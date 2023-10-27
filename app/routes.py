from flask import jsonify, request, abort
from app import app, db
from app.models import *
from app.errors import *


# TODO: Implement
@app.route('/wallets', methods=['GET'])
def get_wallets_info():
    wallets = Wallet.query.all()
    return jsonify([wallet.to_dict() for wallet in wallets]), 200


@app.route('/wallets', methods=['POST'])
def add_wallet():
    name = request.form.get('name')
    respond = dict()
    if name is None:
        return jsonify({'error': 'no name provided'}), 400
    wallet = Wallet.query.filter_by(name=name).first()
    if wallet is not None:
        respond.update({'error': 'a wallet with the given name already exists'})
        return jsonify(respond), 400
    wallet = Wallet(name=name)
    db.session.add(wallet)
    db.session.commit()
    respond.update(wallet.to_dict())
    return jsonify(respond), 201


@app.route('/wallets/<int:wallet_id>', methods=['PUT'])
def edit_wallet_name(wallet_id):
    respond = dict()
    wallet = Wallet.query.filter_by(id=wallet_id).first()
    name = request.form.get('name')
    if wallet is None:
        return jsonify({'error': 'not found'}), 404
    if name is None:
        return jsonify({'error': 'no name provided'}), 400
    if Wallet.query.filter_by(name=name).first():
        respond.update({'error': 'a wallet with the given name already exists'})
        return jsonify(respond), 400
    wallet.name = name
    wallet.updated_at = datetime.utcnow()
    db.session.commit()
    respond.update(wallet.to_dict())
    return jsonify(respond), 200


@app.route('/wallets/<int:wallet_id>', methods=['DELETE'])
def delete_wallet(wallet_id):
    wallet = Wallet.query.filter_by(id=wallet_id).first()
    if wallet is None:
        return jsonify({'error': 'not found'}), 404
    db.session.delete(wallet)
    db.session.commit()
    return jsonify(wallet.to_dict()), 200


@app.route('/coins', methods=['GET'])
def get_coins_info():
    coins = Coin.query.all()
    return jsonify([coin.to_dict() for coin in coins]), 200


@app.route('/coins', methods=['POST'])
def add_coin():
    name = request.form.get('name')
    symbol = request.form.get('symbol')
    price = request.form.get('price')
    if name is None:
        return jsonify({'error': 'no name provided'}), 400
    if symbol is None:
        return jsonify({'error': 'no symbol provided'}), 400
    if price is None:
        return jsonify({'error': 'no price provided'}), 400
    coin = Coin.query.filter_by(name=name).first()
    if coin:
        return jsonify({'error': 'a coin with the given name already exists'}), 400
    coin = Coin.query.filter_by(symbol=symbol).first()
    if coin:
        return jsonify({'error': 'a coin with the given symbol already exists'}), 400
    coin = Coin(name=name, symbol=symbol, price=price)
    db.session.add(coin)
    db.session.commit()
    return jsonify(coin.to_dict()), 201


@app.route('/wallets/<int:wallet_id>/add_coin', methods=['POST'])
def modify_coin_in_wallet(wallet_id):
    wallet = Wallet.query.filter_by(id=wallet_id).first()
    coin_id = request.form.get('coin_id')
    quantity = request.form.get('quantity')
    if wallet is None:
        return jsonify({'error': 'not found'}), 404
    if coin_id is None:
        return jsonify({'error': 'no coin_id provided'}), 400
    coin = Coin.query.filter_by(id=coin_id).first()
    if coin is None:
        return jsonify({'error': 'invalid coin_id'}), 400
    if quantity is None:
        return jsonify({'error': 'no quantity provided'}), 400
    wallet_coin = WalletCoin.query.filter_by(wallet_id=wallet_id, coin_id=coin_id).first()
    if wallet_coin:
        wallet_coin.quantity = quantity
        wallet_coin.updated_at = datetime.utcnow()
        db.session.commit()
    else:
        wallet_coin = WalletCoin(wallet_id=wallet_id, coin_id=coin_id, quantity=quantity)
        db.session.add(wallet_coin)
        db.session.commit()
    return jsonify([wallet.to_dict()]), 200


@app.route('/wallets/<int:wallet_id>/delete_coin', methods=['DELETE'])
def delete_coin_from_wallet(wallet_id):
    wallet = Wallet.query.filter_by(id=wallet_id).first()
    coin_id = request.form.get('coin_id')
    if wallet is None:
        return jsonify({'error': 'not found'}), 404
    if coin_id is None:
        return jsonify({'error': 'no coin_id provided'}), 400
    coin = Coin.query.filter_by(id=coin_id).first()
    if coin is None:
        return jsonify({'error': 'invalid coin_id'}), 400
    wallet_coin = WalletCoin.query.filter_by(wallet_id=wallet_id, coin_id=coin_id).first()
    if wallet_coin is None:
        return jsonify({'error': 'the wallet does not contain the given coin'}), 400
    db.session.delete(wallet_coin)
    db.session.commit()
    return jsonify([wallet.to_dict()]), 200


@app.route('/coins/<int:coin_id>', methods=['PUT'])
def edit_coin_info(coin_id):
    if (coin := Coin.query.filter_by(id=coin_id).first()) is None:
        return jsonify({'error': 'not found'}), 404
    if (name := request.form.get('name')) is None:
        return jsonify({'error': 'no name provided'}), 400
    if (symbol := request.form.get('symbol')) is None:
        return jsonify({'error': 'no symbol provided'}), 400
    if (price := request.form.get('price')) is None:
        return jsonify({'error': 'no price provided'}), 400
    if Coin.query.filter_by(name=name).first():
        return jsonify({'error': 'a coin with the given name already exists'}), 400
    if Coin.query.filter_by(symbol=symbol).first():
        return jsonify({'error': 'a coin with the given symbol already exists'}), 400
    coin.name = name
    coin.symbol = symbol
    coin.price = price
    coin.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify(coin.to_dict()), 200


@app.route('/coins/<int:coin_id>', methods=['DELETE'])
def delete_coin(coin_id):
    coin = Coin.query.filter_by(id=coin_id).first()
    if coin is None:
        return jsonify({'error': 'not found'}), 404
    db.session.delete(coin)
    db.session.commit()
    return jsonify(coin.to_dict()), 200


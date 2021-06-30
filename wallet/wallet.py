# Import dependencies
import subprocess
import json
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
from constants import *
import bit
 
 
# Create a function called `derive_wallets`
def derive_wallets(coin):
    command = f'./derive -g --mnemonic="{mnemonic}"--cols=path,address,privkey,pubkey --format=json --coin="{coin}" --numderive=3'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
    ETH: derive_wallets(ETH),
    BTCTEST: derive_wallets(BTCTEST)
}

print(coins)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == BTCTEST:
        return bit.PrivateKeyTestnet(priv_key) 
    elif coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    else:
        print('Must use either BTCTEST or ETH')
):

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin,account,to,amount):
    if coin == BTCTEST:
        return bit.PrivateKeyTestnet.prepare_transaction(account.address, [(to,amount,BTC)])
    elif coin == ETH:
        
        
        gas_estimate = w3.eth.estimateGas(
            {'from': account.address,'to': to, 'value': amount}
            )
        
        return {
            'from': account.address,
            'to': to,
            'value': amount,
            'gasPrice': w3.eth.gasPrice,
            'gas': gas_estimate,
            'nonce':w3.eth.get.getTransactionCount(account.address)
        }
    
    else:
        print('Must use either BTCTEST or ETH')

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account,to,amount):
    if coin == BTCTEST:
        raw_tx = create_tx(coin,account,to,amount)
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)
    elif coin == ETH:
        raw_tx = create_tx(coin,account,to,amount)
        signed = account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    else:
        print('Must use either BTCTEST or ETH')



btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey)
create_tx(BTCTEST,btc_acc,"mzAVYRCct8qM4pKbUDPr6JJZeC3vsEDMsz", 0.1)
send_txn(BTCTEST,btc_acc,"mzAVYRCct8qM4pKbUDPr6JJZeC3vsEDMsz", 0.1)

#ETH Transaction
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545/0x662541feec10852e7ec7179ad607366c51993142c467765223ba3f7715aed1b3"))
w3.isConnected()
w3.eth.getBalance("0x1445a2385fF2cd7A116F30a9d7d4C4871aA57D3a")
create_tx(ETH,eth_acc,"0x1445a2385fF2cd7A116F30a9d7d4C4871aA57D3a", 1000)
send_txn(ETH, eth_acc,"0x1445a2385fF2cd7A116F30a9d7d4C4871aA57D3a", 1000)
w3.eth.getBalance("0x1445a2385fF2cd7A116F30a9d7d4C4871aA57D3a")


''' S I M P L E   B L O C K C H A I N '''

import datetime
import hashlib 
import json 
from flask import Flask, jsonify 


''' BUILDING THE BLOCKCHAIN '''

class Blockchain:

    def __init__(self):
        self.chain = [] 
        self.create_block(proof=1, previous_hash='0') 

    ''' Create a Block '''
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1, 
                 'timestamp': str(datetime.datetime.now()), 
                 'proof': proof, 
                 'previous_hash': previous_hash 
                 }
        self.chain.append(block)
        return block 

    ''' Get the Last Block of the Chain '''
    def get_previous_block(self):
        return self.chain[-1] 

    ''' "Proof of Work (PoW)" 
        is the number or piece of data the miners need to find in order to create a new "block" '''
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
    
            if hash_operation[:4] == '0000': 
                check_proof = True           
            else:
                new_proof += 1 
        return new_proof  

    ''' Hash of the Block '''
    def hash(self, block):
        encoded_block = json.dumps(block,sort_keys=True).encode()  
        return hashlib.sha256(encoded_block).hexdigest()

    ''' Check if all the Blocks in the Chain are valid '''
    def is_chain_valid(self, chain): 
        previous_block = chain[0] 
        block_index = 1 

        while block_index < len(chain):  
            current_block = chain[block_index]  
            if current_block['previous_hash'] != self.hash(previous_block):
                return False  

            previous_proof = previous_block['proof'] 
            proof = current_block['proof'] 
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            
            if hash_operation[:4] != '0000':
                return False

            previous_block = current_block  
            block_index += 1  
        return True


''' BUILDING THE MINING '''

''' Create Web App working with API in order to interact wuth the code '''
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

''' Get the Blockchain instance '''
blockchain = Blockchain() 

''' Mining New Block '''
@app.route('/mine_block', methods = ['GET'])
def mine_block():
   
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message': 'Congratulation! You just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200 


''' MINE BLOCK / GET BLOCK '''

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'lenght': len(blockchain.chain)}
    return jsonify(response), 200

''' Check Blockchain is Valid '''
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'THE CHAIN WORKS PERFECTLY WITH NO ERRORS OR BUGS!'}
    else:
        response = {'message': '⚠ WE GOT A PROBLEM HERE'}
    return jsonify(response), 200

''' Running the App '''
app.run(host = '0.0.0.0', port = 5000)


''' RESULT '''

''' Get the last block '''

    # to See the Chain RUN ON >>> http://192.168.1.66:5000/get_chain
    # OUTPUT =
    # {
    #     "chain": [
    #         {
    #             "index": 1,
    #             "previous_hash": "0",
    #             "proof": 1,
    #             "timestamp": "2022-01-10 21:41:07.952341"
    #         }
    #     ],
    #     "lenght": 1
    # }

''' Mine new block '''

    # to Mine a Block RUN ON >>> http://192.168.1.66:5000/mine_block
    # OUTPUT =
    # {
    #     "index": 2,
    #     "message": "Congratulation! You just mined a block!",
    #     "previous_hash": "84e49e76b8ba491e75dcd398136d15b28912c540f8eea3999d295c0c0ccd19ba",
    #     "proof": 533,
    #     "timestamp": "2022-01-10 21:45:23.555679"
    # }
    
''' Check the chain status '''

    # to Check is_valid RUN ON >>> http://192.168.1.66:5000/is_valid
    # OUTPUT = 
    # {
    #    "message": "THE CHAIN WORKS PERFECTLY WITH NO ERRORS OR BUGS!"
    # }

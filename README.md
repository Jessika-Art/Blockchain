# Blockchain

This simple blockchain allows you to mine new blocks, show the blocks anc check the blocks.


''' Get the last block '''

    # to See the Chain RUN ON >>> http://your_IP_address/get_chain
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

    # to Mine a Block RUN ON >>> http://your_IP_address/mine_block
    # OUTPUT =
    # {
    #     "index": 2,
    #     "message": "Congratulation! You just mined a block!",
    #     "previous_hash": "84e49e76b8ba491e75dcd398136d15b28912c540f8eea3999d295c0c0ccd19ba",
    #     "proof": 533,
    #     "timestamp": "2022-01-10 21:45:23.555679"
    # }
    
''' Check the chain status '''

    # to Check is_valid RUN ON >>> http://your_IP_address/is_valid
    # OUTPUT = 
    # {
    #    "message": "THE CHAIN WORKS PERFECTLY WITH NO ERRORS OR BUGS!"
    # }

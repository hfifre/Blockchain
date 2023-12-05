from Blockchain import Blockchain

blockchain = Blockchain()

blockchain.create_block_in_chain("le premier")
blockchain.create_block_in_chain("faut test hein")
blockchain.create_block_in_chain("un petit dernier")

blockchain.display_blockchain()
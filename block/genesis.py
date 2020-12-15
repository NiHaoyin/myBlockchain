from block import block

def gen_genesis():
    genesis_block = block(0)  # the previous hash value of genesis is set to 0
    return genesis_block


    
def LFSR(seed, taps, length):

    stream = ''
    print '\n'
    for i in range(length):

        xor = 0
        
        # xoring together all the tap values
        for tap in taps:
            xor = int(seed[tap-1], 2)^xor

        # adding the last bit to the stream variable    
        stream += seed[-1:] 
        
        # rightwards bit shifting 
        binary_part = bin(int(seed , 2) >> 1).replace('0b', '')
        next_seed_part = '0' * (len(seed) - len(binary_part)-1) + binary_part
        print seed + ' ' + stream

        # assigning new value to the seed variable
        seed = str(xor) + next_seed_part

    return stream

def main():
    
    # taking inputs
    seed = raw_input("Enter the seed value for the LFSR: ")
    taps_number = raw_input("Enter the number of tap values that are going to be used: ")
    taps = []
    print ("Now enter the tap values for your LFSR in differnt lines")
    for i in range(int(taps_number)):
        tap = raw_input()
        taps.append(int(tap))
    stream_len = raw_input("Enter the length of the key-stream you want to get: ")
    print "\nfinal keystream value: " + LFSR(seed,taps,int(stream_len))

if __name__ == "__main__":
    main()
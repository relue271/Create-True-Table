def main():
    qtd = input("in: ")
    print("\nout:\n ")
    
    vet = []
    for i in range(26):
        vet.append(2)

    for j in range(65, qtd+65):
        print(chr(j)),
    print


    for entrada in range(2**qtd):
        if (entrada & 1):
            vet[0] = 1
        else:
            vet[0] = 0
        
        if (entrada & 2):
            vet[1] = 1
        else:
            vet[1] = 0
        
        if (entrada & 4):
            vet[2] = 1
        else:
            vet[2] = 0
        
        if (entrada & 8):
            vet[3] = 1
        else:
            vet[3] = 0
        
        if (entrada & 16):
            vet[4] = 1
        else:
            vet[4] = 0





        if (entrada & 32):
            vet[5] = 1
        else:
            vet[5] = 0
        
        if (entrada & 64):
            vet[6] = 1
        else:
            vet[6] = 0
        
        if (entrada & 128):
            vet[7] = 1
        else:
            vet[7] = 0
        
        if (entrada & 256):
            vet[8] = 1
        else:
            vet[8] = 0
        
        if (entrada & 512):
            vet[9] = 1
        else:
            vet[9] = 0



        if (entrada & 1024):
            vet[10] = 1
        else:
            vet[10] = 0
        
        if (entrada & 2048):
            vet[11] = 1
        else:
            vet[11] = 0
        
        if (entrada & 4096):
            vet[12] = 1
        else:
            vet[12] = 0
        
        if (entrada & 8192):
            vet[13] = 1
        else:
            vet[13] = 0
        
        if (entrada & 16384):
            vet[14] = 1
        else:
            vet[14] = 0






        if (entrada & 32768):
            vet[15] = 1
        else:
            vet[15] = 0
        
        if (entrada & 65536):
            vet[16] = 1
        else:
            vet[16] = 0
        
        if (entrada & 131072):
            vet[17] = 1
        else:
            vet[17] = 0
        
        if (entrada & 262144):
            vet[18] = 1
        else:
            vet[18] = 0
        
        if (entrada & 524288):
            vet[19] = 1
        else:
            vet[19] = 0




        if (entrada & 1048576):
            vet[20] = 1
        else:
            vet[20] = 0
        
        if (entrada & 2097152):
            vet[21] = 1
        else:
            vet[21] = 0
        
        if (entrada & 4194304):
            vet[22] = 1
        else:
            vet[22] = 0
        
        if (entrada & 8388608):
            vet[23] = 1
        else:
            vet[23] = 0
        
        if (entrada & 16777216):
            vet[24] = 1
        else:
            vet[24] = 0

        if (entrada & 33554432):
            vet[25] = 1
        else:
            vet[25] = 0


        for j in range(qtd):
            print(vet[j]),
        print

    return

main()

import getopt, sys

memory = [] #changing memory
instruction = []
instrName = []
address = []
opcode = []
valid = []
arg1 = []
arg2 = []
arg3 = []
dest = []
src1 = []
src2 = []
PC = 96
numInstructions = 0 #includes BREAK
filler = -1

class disClass:
    def __init__( self ):
        pass

    def disassemble( self ):
        global filler
        global numInstructions
        i = 0
        while True:

            opcode.append(int(instruction[i][1:6],2))
            valid.append(int(instruction[i][0]))

            if instruction[i][0:1] == '0':
                ###work
                instrName.append('Invalid Instruction')
                address.append(PC + (i * 4))
                arg1.append(int(instruction[i][6:11],2))
                arg2.append(int(instruction[i][11:16],2))
                arg3.append('')
                dest.append(filler)
                filler-=1
                src1.append(filler)
                filler-=1
                src2.append(filler)
                filler-=1
                numInstructions+=1
                i = i + 1
            else:
                #opcode 0
                if (instruction[i][0:32] == '10000000000000000000000000001101'): #break
                    instrName.append( 'BREAK')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))
                    arg2.append(int(instruction[i][11:16],2))
                    arg3.append(0)
                    dest.append(filler)
                    filler-=1
                    src1.append(filler)
                    filler-=1
                    src2.append(filler)
                    filler-=1
                    numInstructions+=1
                    i = i + 1
                    break;
                elif opcode[i] == 0:

                    if instruction[i][26:32] == '000000': 
                        if instruction[i][1:32] == '0000000000000000000000000000000':#nop
                            instrName.append( 'NOP')
                            address.append(PC + (i * 4))
                            arg1.append(int(instruction[i][6:11],2))
                            arg2.append(int(instruction[i][11:16],2))
                            arg3.append('')
                            dest.append(filler)
                            filler-=1
                            src1.append(filler)
                            filler-=1
                            src2.append(filler)
                            filler-=1
                            numInstructions+=1
                            i = i + 1
                        else: #SLL Format: SLL rd, rt, sa
                            instrName.append( 'SLL')
                            address.append(PC + (i * 4))
                            arg1.append(int(instruction[i][11:16],2))#rt
                            arg2.append(int(instruction[i][16:21],2))#rd
                            arg3.append(int(instruction[i][21:26],2))#sa
                            dest.append(arg2[i])
                            src1.append(arg1[i])
                            src2.append(filler) 
                            filler-=1
                            numInstructions+=1
                            i = i + 1
                            
                    elif instruction[i][26:32] == '000010': #SRL Format: SRL rd, rt, sa
                        instrName.append( 'SRL')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][11:16],2))#rt
                        arg2.append(int(instruction[i][16:21],2))#rd
                        arg3.append(int(instruction[i][21:26],2))#sa
                        dest.append(arg2[i])
                        src1.append(arg1[i])
                        src2.append(filler) 
                        filler-=1
                        numInstructions+=1
                        i = i + 1
                        #dfile.write( '\tSRL\tR' + str(rt) + ', R' + str(rd) + ', #' + str(sa) + '\n')
                    
                    elif instruction[i][26:32] == '001000': #JR Format: JR rs
                        instrName.append( 'JR')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))
                        arg2.append(0)
                        arg3.append(0)
                        dest.append(filler) 
                        filler-=1
                        src1.append(arg1[i])
                        src2.append(filler) 
                        filler-=1
                        numInstructions+=1
                        i = i + 1
                        #dfile.write( '\tJR\tR' + str(rs))

                    elif instruction[i][26:32] == '001010': #MOVZ Format: MOVZ rd, rs, rt
                        instrName.append( 'MOVZ')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
                        #dfile.write( '\tMOVZ\tR' + str(rd) + ', R' + str(rs) + ', R' + str(rt) + '\n')

                    elif instruction[i][26:32] == '100000': #ADD Format: ADD rd, rs, rt
                        instrName.append( 'ADD')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
           
                    elif instruction[i][26:32] == '100010': #SUB Format: SUB rd, rs, rt
                        instrName.append( 'SUB')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
               
                    elif instruction[i][26:32] == '100100': #AND Format: AND rd, rs, rt
                        instrName.append( 'AND')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1
                 
                    elif instruction[i][26:32] == '100101': #OR Format: OR rd, rs, rt
                        instrName.append( 'OR')
                        address.append(PC + (i * 4))
                        arg1.append(int(instruction[i][6:11],2))#rs
                        arg2.append(int(instruction[i][11:16],2))#rt
                        arg3.append(int(instruction[i][16:21],2))#rd
                        dest.append(arg3[i])
                        src1.append(arg1[i])
                        src2.append(arg2[i])
                        numInstructions+=1
                        i = i + 1

                #opcode 1
                elif opcode[i] == 1: #BLTZ Format: BLTZ rs, offset
                    instrName.append( 'BLTZ')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#BLTZ
                    arg3.append(int(instruction[i][16:32],2))#offset
                    if instruction[i][16:17] == '1':
                        arg3[i] = ((arg3[i] ^ 0b1111111111111111) + 1) * -1
                    dest.append(filler) 
                    filler-=1
                    src1.append(arg1[i])
                    src2.append(filler) 
                    filler-=1
                    
                    numInstructions+=1
                    i = i + 1

              
                #opcode 2
                elif opcode[i] == 2: #J
                    instrName.append('J')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:32],2) * 4) #shifted left two
                    arg2.append(0)
                    arg3.append(0)
                    dest.append(filler) 
                    filler-=1
                    src1.append(filler) 
                    filler-=1
                    src2.append(filler) 
                    filler-=1
                    numInstructions+=1
                    i = i + 1 
                    
                #opcode 4
                elif opcode[i] == 4: #BEQ Format: BEQ rs, rt, offset
                    instrName.append('BEQ')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#offset
                    if instruction[i][16:17] == '1':
                        arg3[i] = ((arg3[i] ^ 0b1111111111111111) + 1) * -1
                    dest.append(filler) 
                    filler-=1
                    src1.append(arg1[i])
                    src2.append(arg2[i])
                    numInstructions+=1
                    i = i + 1

                #opcode 8
                elif opcode[i] == 8: #ADDI Format: ADDI rt, rs, immediate
                    instrName.append( 'ADDI')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#immediate
                    if instruction[i][16:17] == '1':
                        arg3[i] = ((arg3[i] ^ 0b1111111111111111) + 1) * -1
                    dest.append(arg2[i])
                    src1.append(arg1[i])
                    src2.append(filler) 
                    filler-=1
                    numInstructions+=1
                    i = i + 1 
                 
                #opcode 0x2b
                elif opcode[i] == 11: #SW Format: SW rt, offset(base)
                    instrName.append( 'SW')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#base
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#offset
                    if instruction[i][16:17] == '1':
                        arg3[i] = ((arg3[i] ^ 0b1111111111111111) + 1) * -1
                    dest.append(filler) 
                    filler-=1
                    src1.append(arg2[i])
                    src2.append(arg1[i]) 
                    numInstructions+=1
                    i = i + 1 
                #opcode 0x23
                elif opcode[i] == 3: #LW Format: LW rt, offset(base)
                    instrName.append( 'LW')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#base
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:32],2))#offset
                    if instruction[i][16:17] == '1':
                        arg3[i] = ((arg3[i] ^ 0b1111111111111111) + 1) * -1
                    dest.append(arg2[i])
                    src1.append(arg1[i]) 
                    src2.append(filler) 
                    filler-=1
                    numInstructions+=1
                    i = i + 1
                #opcode 0x1C
                elif opcode[i] == 28: #MUL Format: MUL rd, rs, rt
                    instrName.append( 'MUL')
                    address.append(PC + (i * 4))
                    arg1.append(int(instruction[i][6:11],2))#rs
                    arg2.append(int(instruction[i][11:16],2))#rt
                    arg3.append(int(instruction[i][16:21],2))#rd
                    dest.append(arg3[i])
                    src1.append(arg1[i])
                    src2.append(arg2[i])
                    numInstructions+=1
                    i = i + 1
                
        j = 0
        while i < len(instruction):
            address.append(PC + (i * 4))
            memory.append(int(instruction[i],2))
            if instruction[i][0:1] == '1':
                memory[j] = (((memory[j] ^ 0b11111111111111111111111111111111) + 1) * -1)
            i+=1
            j+=1

    def printDis(self, dfile):
        i = 0
        while i < numInstructions:
            dfile.write( str(instruction[i][0:1]) + ' ' + str(instruction[i][1:6]) + ' ' + str(instruction[i][6:11]) + ' ' + str(instruction[i][11:16]))
            dfile.write( ' ' + str(instruction[i][16:21]) + ' ' + str(instruction[i][21:26]) + ' ' + str(instruction[i][26:32]) + '\t' + str(address[i]))
            
            if instrName[i] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR', 'MUL']:
                dfile.write( '\t' + instrName[i] + '\tR'+ str(arg3[i]) + ', R' + str(arg1[i]) + ', R' + str(arg2[i]) + '\n')
            elif instrName[i] in ['SLL', 'SRL']:
                dfile.write( '\t' + instrName[i] + '\tR' + str(arg1[i]) + ', R' + str(arg2[i]) + ', #' + str(arg3[i]) + '\n')
            elif instrName[i] in ['BEQ', 'ADDI']:
                dfile.write( '\t' + instrName[i] + '\tR' + str(arg2[i]) + ', R' + str(arg1[i]) + ', #' + str(arg3[i]) + '\n')
            elif instrName[i] in ['SW', 'LW']:
                dfile.write( '\t' + instrName[i] + '\tR' + str(arg2[i]) + ', ' + str(arg3[i]) + '(R' + str(arg1[i]) + ')\n')
            elif instrName[i] == 'BLTZ':
                dfile.write( '\tBLTZ\tR' + str(arg1[i]) + ', #' + str(arg3[i]) + '\n')
            elif instrName[i] == 'J':
                dfile.write( '\tJ\t#' + str(arg1[i]) + '\n')
            elif instrName[i] == 'JR':
                dfile.write( '\tJR\tR' + str(arg1[i]) + '\n')
            elif instrName[i] in ['NOP', 'BREAK', 'Invalid Instruction']:
                dfile.write( '\t' + instrName[i]+ '\n')
            i += 1
        j = 0
        while i < (len(instruction)):
            dfile.write( str(instruction[i][0:32]) + '\t' + str(address[i]) + '\t' + str(memory[j]) + '\n')
            j += 1 
            i += 1

for i in range( len(sys.argv)):
    if(sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
        inputFileName = sys.argv[i+1]
    elif(sys.argv[i] == '-o' and i < (len(sys.argv) -1)):
        outputFileName = sys.argv[i+1]

f = open( inputFileName, 'r')
disFile = open( outputFileName + "_dis.txt", 'w' )
pipelineFile = open( outputFileName + "_pipeline.txt", 'w' )

words = [] 
for line in f:
    instruction.append(line[0:32])
disassembler = disClass()
disassembler.disassemble()
disassembler.printDis(disFile)

class writeBack:
    def __init__(self):
        #print('initialized wb')
        pass
    def run(self):
        #print('wb running')
        if(sim.postALUBuff[1] != -1):
            sim.R[sim.destReg[sim.postALUBuff[1]]] = sim.postALUBuff[0]
            sim.postALUBuff[0] = -1
            sim.postALUBuff[1] = -1
        if(sim.postMemBuff[1] != -1):
            sim.R[sim.destReg[sim.postMemBuff[1]]] = sim.postMemBuff[0]
            sim.postMemBuff[0] = -1
            sim.postMemBuff[1] = -1

class arithmeticLogicUnit:
    
    def __init__(self):
        #print('initialized ALU')
        pass
    def run(self):
        if (sim.preALUBuff[0] != -1):
            i = sim.preALUBuff[0]
            # sim.postALUBuff[1] = sim.destReg[i]
            sim.postALUBuff[1] = i

            if(sim.instrName[i] == 'SLL'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i]] * pow(2,sim.arg3[i])
            elif(sim.instrName[i] == 'SRL'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i]] / pow(2,sim.arg3[i])
            elif(sim.instrName[i] == 'ADDI'):
                sim.postALUBuff[0] = int(sim.R[sim.src1Reg[i]]) + sim.arg3[i]
                # print str(sim.R[sim.src1Reg[i]]+sim.arg3[i])
            elif(sim.instrName[i] == 'MUL'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] * sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'OR'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] | sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'AND'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] & sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'SUB'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i] - sim.R[sim.src2Reg[i]]]
            elif(sim.instrName[i] == 'ADD'):
                sim.postALUBuff[0] = sim.R[sim.src1Reg[i]] + sim.R[sim.src2Reg[i]]
            elif(sim.instrName[i] == 'MOVZ'):
                if(sim.src2Reg[i] == 0):
                    sim.postALUBuff[0] = sim.src1Reg[i]

            sim.preALUBuff[0] = sim.preALUBuff[1]
            sim.preALUBuff[1] = -1
        else:
            #print('not doing ALU stuff')
            pass

class memWrite:
    def __init__(self):
        #print('initialized MEM')
        pass
    def run(self):
        #print('MEM running')
        if(sim.preMemBuff[0] != -1):
            i = sim.preMemBuff[0]
            hit = False
            if(sim.instrName[i] == 'LW'):
                address = sim.arg3[i] + sim.R[sim.src1Reg[i]] #offset + base
                hit, data = sim.cache.accessMemory(sim.getIndexOfMemAddress(address),-1,False,0)

            elif(sim.instrName[i] == 'SW'):
                address = sim.arg3[i] + sim.R[sim.src2Reg[i]]
                print 'PASSING THIS TO CACHE' + str(sim.R[sim.src1Reg[i]])
                if sim.R[sim.src1Reg[i]] < 0:
                    passString = bin(((sim.R[sim.src1Reg[i]] * -1) ^ 0b11111111111111111111111111111111) + 1)
                else:
                    passString = bin(sim.R[sim.src1Reg[i]])
                print 'LOOK HERE'+ passString
                hit, data = sim.cache.accessMemory(sim.getIndexOfMemAddress(address), -1, True, sim.R[sim.src1Reg[i]])

            if(hit):
                # intdata = int(str(data),2)
                # if data[0:1] == '1':
                    # intdata = (((int(data,2) ^ 0b11111111111111111111111111111111) + 1) * -1)
                # if(data[0] == '1'):
                #     sim.postMemBuff[0] = ((int(data,2) ^ 0b11111111111111111111111111111111) + 1) * -1
                # else: 
                #     sim.postMemBuff[0] = int(data,2)
                if sim.instrName[i] == 'LW':
                    sim.postMemBuff[0] = int(data)
                    sim.postMemBuff[1] = i

                sim.preMemBuff[0] = sim.preMemBuff[1]
                sim.preMemBuff[1] = -1
            #print 'POST MEM BUFF FROM MEM UNIT: ' + str(sim.postMemBuff)

class issueUnit:
    def __init__(self):
        #print('initialized issue')
        pass
    def run(self):
        issueMe = True
        numIssued = 0
        numInPreIssueBuff = 0
        currIndex = -1
        current = 0

        for i in range(4):
            if(sim.preIssueBuff[i] != -1):
                numInPreIssueBuff += 1

        ##WAR CHECK
        while(numIssued < 2 and numInPreIssueBuff > 0 and current < numInPreIssueBuff):
            issueMe = True
            currIndex = sim.preIssueBuff[current]
            print('issue checking for: ' + sim.instrName[currIndex])
            ## CHECK FOR ROOM IN BUFFERS
            if sim.isMemOp(currIndex) and not -1 in sim.preMemBuff:
                print 'pre mem full'
                issueMe = False
            elif not sim.isMemOp(currIndex) and not -1 in sim.preALUBuff:
                print 'pre alu full'
                issueMe = False

            ## WAR CHECK    
            if current > 0:
                for i in range(0,current):
                    if (sim.destReg[currIndex] == sim.src1Reg[sim.preIssueBuff[i]] or sim.destReg[currIndex] == sim.src2Reg[sim.preIssueBuff[i]]):
                        issueMe = False
                        # break
            if sim.isMemOp(currIndex):
                for i in range(0, len(sim.preMemBuff)):
                    if sim.preMemBuff[i] != -1:
                        if sim.destReg[currIndex] == sim.src1Reg[sim.preMemBuff[i]] or sim.destReg[currIndex] == sim.src2Reg[sim.preMemBuff[i]]:
                            print 'war fail2'
                            issueMe = False
                            # break
            else: #is ALU op
                for i in range(0, len(sim.preALUBuff)):
                    if sim.preALUBuff[i] != -1:
                        if sim.destReg[currIndex] == sim.src1Reg[sim.preALUBuff[i]] or sim.destReg[currIndex] == sim.src2Reg[sim.preALUBuff[i]]:
                            print 'war fail3'
                            issueMe = False
                            # break
            ## RAW CHECK
            if current > 0:
                for i in range(0,current):
                    if (sim.src1Reg[currIndex] == sim.destReg[sim.preIssueBuff[i]] or sim.src2Reg[currIndex] == sim.destReg[sim.preIssueBuff[i]]):
                        issueMe = False
                        # break
            
            for i in range(0, len(sim.preMemBuff)):
                if sim.preMemBuff[i] != -1:
                    if sim.src1Reg[currIndex] == sim.destReg[sim.preMemBuff[i]] or sim.src2Reg[currIndex] == sim.destReg[sim.preMemBuff[i]]:
                        issueMe = False
                        # break
            for i in range(0, len(sim.preALUBuff)):
                if sim.preALUBuff[i] != -1:
                    if sim.src1Reg[currIndex] == sim.destReg[sim.preALUBuff[i]] or sim.src2Reg[currIndex] == sim.destReg[sim.preALUBuff[i]]:
                        issueMe = False
                        # break

            if sim.postALUBuff[1] != -1:
                if sim.src1Reg[currIndex] == sim.destReg[sim.postALUBuff[1]] or sim.src2Reg[currIndex] == sim.destReg[sim.postALUBuff[1]]:
                    #found RAW in post ALU Buffer
                    issueMe = False
            if sim.postMemBuff[1] != -1:
                if sim.src1Reg[currIndex] == sim.destReg[sim.postMemBuff[1]] or sim.src2Reg[currIndex] == sim.destReg[sim.postMemBuff[1]]:
                    #found RAW in post mem Buffer
                    issueMe = False
           
            ## WAW CHECK
            for i in range(0, current):
                if sim.destReg[currIndex] == sim.destReg[sim.preIssueBuff[i]]:
                    issueMe = False

            for i in range(0, len(sim.preMemBuff)):
                if sim.preMemBuff[i] != -1:
                    if sim.destReg[currIndex] == sim.destReg[sim.preMemBuff[i]]:
                        #print 'waw fail1'
                        issueMe = False
                        # break
            for i in range(0, len(sim.preALUBuff)):
                if sim.preALUBuff[i] != -1:
                    if sim.destReg[currIndex] == sim.destReg[sim.preALUBuff[i]]:
                        print 'waw fail2'
                        issueMe = False
                        # break
            if sim.postALUBuff[1] != -1:
                if sim.destReg[currIndex] == sim.destReg[sim.postALUBuff[1]]:
                    #found WAW in post ALU Buffer
                    #print 'waw fail3'
                    issueMe = False
            if sim.postMemBuff[1] != -1:
                if sim.destReg[currIndex] == sim.destReg[sim.postMemBuff[1]]:
                    #found RAW in post ALU Buffer
                    #print 'waw fail4'
                    issueMe = False
        
            ##ENFORCE ORDERING OF LW SW
            #Enforce ordering of LWs and SWs so we make sure all stores are done before loads
            if(sim.instrName[currIndex] == 'LW'):
                for i in range(0, current):
                    if sim.instrName[sim.preIssueBuff[i]] == 'SW':
                        issueMe = False

            ##ISSUE AND MOVE INSTRUCTIONS DOWN ONE LEVEL
            if issueMe:
                numIssued += 1
                if sim.isMemOp(currIndex):
                    sim.preMemBuff[sim.preMemBuff.index(-1)] = currIndex
                else:
                    sim.preALUBuff[sim.preALUBuff.index(-1)] = currIndex

                sim.preIssueBuff[current:3] = sim.preIssueBuff[current+1:]
                sim.preIssueBuff[3] = -1
                numInPreIssueBuff -= 1
            else: 
                current += 1

class instructionFetch:
    cleanup = False
    noHazards = True
    wait = -1

    def __init__(self):
        pass

    def checkForBranchHazards(self, index):
        print 'post mem buff in IF' +str(sim.postMemBuff)
        for i in range(4):
            if sim.preIssueBuff[i] != -1:
                if sim.src1Reg[index] == sim.destReg[sim.preIssueBuff[i]]:
                    print 'branch hazard found in preIssueBuff'
                    self.noHazards = False
        if(sim.preMemBuff[0] != -1):
            if sim.src1Reg[index] == sim.destReg[sim.preMemBuff[0]]:
                print 'branch hazard found in premembuff 0'
                self.noHazards = False
        if(sim.preMemBuff[1] != -1):
            if sim.src1Reg[index] == sim.destReg[sim.preMemBuff[1]]:
                print 'branch hazard found in premembuff 1'
                self.noHazards = False
        if(sim.preALUBuff[0] != -1):
            if sim.src1Reg[index] == sim.destReg[sim.preALUBuff[0]]:
                print 'branch hazard found in prealubuff 0'
                self.noHazards = False
        if(sim.preALUBuff[1] != -1):
            if sim.src1Reg[index] == sim.destReg[sim.preALUBuff[1]]:
                print 'branch hazard found in prealubuff 1'
                self.noHazards = False
        if(sim.postALUBuff[1] != -1):
            if sim.src1Reg[index] == sim.destReg[sim.postALUBuff[1]]:
                print 'branch hazard found in postalubuff'
                self.noHazards = False
        if(sim.postMemBuff[1] != -1):
            print sim.destReg[sim.postMemBuff[1]]
            print sim.src1Reg[index]
            if sim.src1Reg[index] == sim.destReg[sim.postMemBuff[1]]:
                print 'branch hazard found in post mem buff'
                self.noHazards = False

        if self.noHazards:
            print 'no hazards found beepboop'
            print sim.preIssueBuff
            print sim.preMemBuff
        if sim.instrName[index] == 'BLTZ':
            if self.noHazards:
                print 'index, reg contents'
                print sim.src1Reg[index],
                print sim.R[sim.src1Reg[index]];
                if sim.R[sim.src1Reg[index]] < 0:
                    sim.PC += (sim.arg3[index] + 4)
                    print 'BLTZ1, PC NOW ' + str(sim.PC)
                    # return True
                else: 
                    sim.PC += 4
        if sim.instrName[index] == 'BEQ':
            if sim.src2Reg[index] in [sim.destReg[sim.preALUBuff[0]], sim.destReg[sim.preMemBuff[0]],sim.destReg[sim.preMemBuff[1]],sim.destReg[sim.preALUBuff[1]]]:
                print 'branch hazard 5 found'
                self.noHazards = False
            if self.noHazards:
                if(sim.R[sim.src1Reg[index]] == sim.R[sim.src2Reg[index]]):
                    sim.PC += sim.arg3[i]
                    sim.PC += 4
                    print 'BEQ1, PC NOW ' + str(sim.PC)
                    return True
                else:
                    sim.PC += 4

    def run(self):
        index = (sim.PC - 96) / 4
        index1 = index
        numInPre = 0
        numIssued = 0

        for i in range(len(sim.preIssueBuff)):
            if sim.preIssueBuff[i] != -1:
                numInPre += 1

        if not self.cleanup and numInPre < 4: #1
            hit, data1 = sim.cache.accessMemory(-1, index, 0, 0)
        
            if hit and (sim.PC % 8 == 0) and not self.cleanup and numInPre < 4:
                data2 = sim.instruction[index + 1]
                self.noHazards = True
                print 'hittt'
                #check for branching, check for hazards
                if(sim.instrName[index] in ['BEQ', 'BLTZ']):
                    self.checkForBranchHazards(index)
                #if jump, jump (no checking)
                elif(sim.instrName[index] == 'J'):
                    sim.PC = sim.arg1[index] 
                    numIssued += 1
                    print 'J,  PC NOW ' + str(sim.PC)
                    # return True
                elif(sim.instrName[index] == 'JR'):
                    sim.PC = sim.R[sim.src1Reg[index]]
                    print 'JR1,  PC NOW ' + str(sim.PC)
                    # return True
                elif(sim.instrName[index] == 'Invalid Instruction'):
                    sim.PC += 4
                elif(sim.instrName[index] == 'BREAK'):
                    self.cleanup = True
                    self.wait = 1
                else:#some regular instruction
                    print' adding to premem buff'
                    sim.preIssueBuff[numInPre] = index
                    sim.PC += 4
                    numInPre += 1

                if(((sim.PC - 96) /4) == index + 1) and numInPre < 4:
                    index = index + 1
                    if(sim.instrName[index] in ['BLTZ', 'BEQ']):
                        self.checkForBranchHazards(index)
                    #if jump, jump (no checking)
                    elif(sim.instrName[index] == 'J'):
                        sim.PC = sim.arg1[index] 
                        numIssued += 1
                        print 'J,  PC NOW ' + str(sim.PC)
                        # return True
                    elif(sim.instrName[index] == 'JR'):
                        sim.PC = sim.R[sim.src1Reg[index]]
                        print 'JR1,  PC NOW ' + str(sim.PC)
                        # return True
                    elif(sim.instrName[index] == 'Invalid Instruction'):
                        sim.PC += 4
                    elif(sim.instrName[index] == 'BREAK'):
                        self.cleanup = True
                        self.wait = 1
                    else:#some regular instruction

                        sim.preIssueBuff[numInPre] = index
                        sim.PC += 4
                        numInPre += 1

            elif hit and not self.cleanup and numInPre < 4:
                print 'hittt 2'
                self.noHazards = True
                #check for branching, check for hazards
                if(sim.instrName[index] in ['BLTZ', 'BEQ']):
                    self.checkForBranchHazards(index)
                #if jump, jump (no checking)
                elif(sim.instrName[index] == 'J'):
                    sim.PC = sim.arg1[index] 
                    numIssued += 1
                    print 'J,  PC NOW ' + str(sim.PC)
                    # return True
                elif(sim.instrName[index] == 'JR'):
                    sim.PC = sim.R[sim.src1Reg[index]]
                    print 'JR1,  PC NOW ' + str(sim.PC)
                    # return True
                elif(sim.instrName[index] == 'Invalid Instruction'):
                    sim.PC += 4
                elif(sim.instrName[index] == 'BREAK'):
                    self.cleanup = True
                    self.wait = 1
                else:#some regular instruction
                    sim.preIssueBuff[numInPre] = index
                    sim.PC += 4
                    numInPre += 1

        if(self.cleanup):
            print 'cleaning up...'
            print sim.preIssueBuff
            print sim.preALUBuff
            print sim.postMemBuff
            print sim.postALUBuff
            for i in range(4):
                if sim.preIssueBuff[i] != -1:
                    print 'cleaning up preissue'
                    return True
            if (sim.preMemBuff[0] != -1) or (sim.preMemBuff[1] != -1) or (sim.preALUBuff[0] != -1) or (sim.preALUBuff[1] != -1):
                print 'cleaning up pre buffers'
                self.wait = 1
                return True
            elif (sim.postMemBuff[1] != -1 or sim.postALUBuff[1] != -1):
                print 'cleaning up post buffers'
                self.wait = 1
                return True
            elif (sim.instrName[index1] not in ['BLTZ', 'BEQ', 'J', 'JR']):
                self.wait -= 1
            # #waits one cycle for stuff to WB clean up, then stops
            if(self.wait == 1):
                self.wait -= 1
                print sim.preALUBuff
                print sim.postALUBuff
                print sim.preMemBuff
                print sim.postMemBuff
                return True
            else:
                return False
            if(self.wait == 0):
                return False
        if(sim.cycle >100): 
            return False
        return True

    
class cacheUnit:
    cacheSet = [[[0,0,0,0,0],[0,0,0,0,0]], #valid,dirty,tag,data,data
                [[0,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0]]]
    lruBit = [0,0,0,0] #one for each SET
    tagMask = int('00000000000000000000000011111111',2)
    # 96 = 01100000 set 0, tag 3
    setMask = int('0011111',2)
    justMissedList = [-1,-1] #1st is instruction, second is mem

    def __init__(self):
        pass

    def flush(self): #deprecated
        for s in range(4):
            if(self.cacheSet[s][0][1] == 1):#if first block claims dirty
                wbAddr = self.cacheSet[s][0][2] #tag of mem
                wbAddr = (wbAddr << 5) + (s << 3) #converted to address with s
                index = (wbAddr - 96 - ( 4 * sim.numInstructions))/4 #index of mem
                if(sim.memory[index] == self.cacheSet[s][0][3] and sim.memory[index+1] == self.cacheSet[s][0][4]):
                    # self.cacheSet[s][0][1] = 0 #reset dirty bit
                    pass
                else:
                    sim.memory[index] = self.cacheSet[s][0][3] #change value in memory 1st word
                    sim.memory[index + 1] = self.cacheSet[s][0][4] #change value in memory 2nd word
            elif (self.cacheSet[s][1][1] == 1): 
                print s
                wbAddr = self.cacheSet[s][1][2]
                wbAddr = (wbAddr << 5) + (s << 3)
                index = (wbAddr - 96 - ( 4 * sim.numInstructions))/4
                if(sim.memory[index] == self.cacheSet[s][1][3] and sim.memory[index+1] == self.cacheSet[s][1][4]):
                    # self.cacheSet[s][1][1] = 0 #reset dirty bit
                    pass
                else:
                    sim.memory[index] = self.cacheSet[s][1][3] #change value in memory 1st word
                    sim.memory[index + 1] = self.cacheSet[s][1][4] #change value in memory 2nd word
                # self.cacheSet[s][1][1] = 0
    
    def finalFlush(self):
        for s in range(4):
            if(self.cacheSet[s][0][2]==1):
                wbAddr = self.cacheSet[s][0][2] #tag of mem
                wbAddr = (wbAddr << 5) + (s << 3) #converted to address with s
                index = (wbAddr - 96 - ( 4 * sim.numInstructions))/4 #index of mem
                self.cacheSet[s][0][1] = 0 #reset dirty bit
                sim.memory[index] = self.cacheSet[s][0][3] #change value in memory 1st word
                sim.memory[index + 1] = self.cacheSet[s][0][4] #change value in memory 2nd word
            elif (self.cacheSet[s][1][1] == 1): 
                wbAddr = self.cacheSet[s][1][2]
                wbAddr = (wbAddr << 5) + (s << 3)
                index = (wbAddr - 96 - ( 4 * sim.numInstructions))/4
                self.cacheSet[s][1][1] = 0 #reset dirty bit
                sim.memory[index] = self.cacheSet[s][1][3] #change value in memory 1st word
                sim.memory[index + 1] = self.cacheSet[s][1][4] #change value in memory 2nd word
                self.cacheSet[s][1][1] = 0

    def accessMemory(self, memIndex, instrIndex, isWriteTomem, dataToWrite):
        #figure out the alignment
        if(instrIndex != -1):
            address = (instrIndex * 4) + 96
            if(address % 8 == 0): #address 96+n8
                dataword = 0 #block 0 was the address
                address1 = address
                address2 = address + 4
            else: #address != 96+n8
                dataword = 1 #block 1 was the address
                address1 = address - 4
                address2 = address
            data1 = sim.instruction[(address1 - 96) / 4]
            data2 = sim.instruction[(address2 - 96) / 4]
        else:
            address = (memIndex * 4) + 96 + (4 * sim.numInstructions)
            if(address % 8 == 0): #address 96+n8
                dataword = 0 #block 0 was the address
                address1 = address
                address2 = address + 4
            else: #address != 96+n8
                dataword = 1 #block 1 was the address
                address1 = address - 4
                address2 = address
            data1 = sim.memory[(address1 - (96 + (4 * sim.numInstructions))) / 4]
            data2 = sim.memory[(address2 - (96 + (4 * sim.numInstructions))) / 4]

        #4
        if(isWriteTomem and dataword == 0):
            data1 = dataToWrite
        elif(isWriteTomem and dataword == 1):
            data2 = dataToWrite

        #5. decode the address of word 0 into cache address
        tag =  (address1 & self.tagMask)
        setNum = (tag & self.setMask) >> 3
        tag = tag >> 5

        hit = False

        if(self.cacheSet[setNum][0][2] == tag):
            assocblock = 0
            hit = True 
        elif(self.cacheSet[setNum][1][2] == tag):
            assocblock = 1
            hit = True
        print 'hit = ' + str(hit)
        if(hit and isWriteTomem):
            #update dirty bit
            self.cacheSet[setNum][assocblock][1] = 1 
            #update set lru bit
            self.lruBit[setNum] = (assocblock + 1) % 2
            #write data to cache
            self.cacheSet[setNum][assocblock][dataword + 3] = dataToWrite
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        #8.
        elif(hit and not isWriteTomem):
            self.lruBit[setNum] = (assocblock + 1) % 2
            return True, self.cacheSet[setNum][assocblock][dataword + 3]
        #9. 
        elif(not hit):
            if(address1 not in self.justMissedList):
                if(memIndex != -1):
                    self.justMissedList[1] = address1
                else:
                    self.justMissedList[0] = address1
                print('just missed: ' + str(self.justMissedList))
                return False, 0
            else: #second miss
                if self.cacheSet[setNum][ self.lruBit[setNum] ][1] == 1:
                    # write back the memory address asociated with the block
                    wbAddr = self.cacheSet[setNum][ self.lruBit[setNum] ][2] #tag

                    wbAddr = (wbAddr << 5) +( setNum << 3)

                    if( wbAddr >= (sim.numInstructions  *4) + 96 ):
                        sim.memory[ sim.getIndexOfMemAddress(wbAddr) ] = self.cacheSet[setNum][ self.lruBit[setNum] ][3]
                    if( wbAddr+4 >= (sim.numInstructions  *4) + 96 ):
                        sim.memory[ sim.getIndexOfMemAddress(wbAddr+4) ] = self.cacheSet[setNum][ self.lruBit[setNum] ][4]
                    # now update the cache flag bits
                self.cacheSet[setNum][ self.lruBit[setNum] ][0] = 1 #valid  we are writing a block
                self.cacheSet[setNum][ self.lruBit[setNum] ][1] = 0 #reset the dirty bit
                if( isWriteTomem ):
                    self.cacheSet[setNum][ self.lruBit[setNum] ][1] = 1 #dirty if is data mem is dirty again, intruction mem never dirty
                # update both words in the actual cache block in set
                self.cacheSet[setNum][ self.lruBit[setNum] ][2] = tag #tag
                self.cacheSet[setNum][ self.lruBit[setNum] ][3] = data1 #data
                self.cacheSet[setNum][ self.lruBit[setNum] ][4] = data2 #nextData

                if(memIndex != -1):
                    if type(data1) == str and type(data2) == str:
                        if data1[0] == '1': #if sim.R[sim.src1Reg[i]] < 0:
                            intdata1 = ((int(data1,2) ^ 0b11111111111111111111111111111111) + 1) * -1
                        else:
                            intdata1 = int(data1,2)

                        if data2[0] == '1':
                            intdata2 = ((int(data2,2) ^ 0b11111111111111111111111111111111) + 1) * -1
                        else:
                            intdata2 = int(data2,2)
                        self.cacheSet[setNum][ self.lruBit[setNum] ][3] = intdata1 #nextData
                        self.cacheSet[setNum][ self.lruBit[setNum] ][4] = intdata2 #nextData
                    else:
                        self.cacheSet[setNum][ self.lruBit[setNum] ][3] = data1 #nextData
                        self.cacheSet[setNum][ self.lruBit[setNum] ][4] = data2 
                #print 'SETNUM2: ' + str(setNum)
                self.lruBit[setNum] = (self.lruBit[setNum] + 1) % 2 # set lru to show block is recently used
                print 'from the last return' 
                return [True, self.cacheSet[setNum][(self.lruBit[setNum] + 1) % 2][dataword+3] ]   # dataword was the actual word thatgenerated the hit

class simClass:
    instruction = []
    opcode = []
    memory = []
    validInstr = []
    address = []
    numInstructions = 0
    instrName = []
    arg1 = []
    arg2 = []
    arg3 = []
    destReg = []
    src1Reg = []
    src2Reg = []
    cycle = 1
    PC = 96
    R = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] #registers 0-32 
    WB = writeBack()
    ALU = arithmeticLogicUnit()
    MEM = memWrite()
    issue = issueUnit()
    fetch = instructionFetch()
    cache = cacheUnit()

    preMemBuff = [-1,-1] #first number is index, second is index
    postMemBuff = [-1,-1] #first number is value, scond is instruction index

    preALUBuff = [-1,-1]#first number is index, second is index, 2 instructions
    postALUBuff = [-1,-1]#first number is value, second is instr index

    preIssueBuff = [-1,-1,-1,-1] # list of 4 instruction indices

    def __init__( self, instrs, opcodes, mem, valids, addrs, arg1, arg2, arg3, numInstrs, dest, src1, src2, instrNa ):
        self.instruction = instrs
        self.opcode = opcodes
        self.memory = mem
        self.validInstr = valids
        self.address = addrs
        self.numInstructions = numInstrs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.destReg = dest
        self.src1Reg = src1
        self.src2Reg = src2
        self.instrName = instrNa

    def printState(self):
        global pipelineFile

        formattedInstr = ['','','','','','','','','','']
        indices = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        for i in range(4):
            indices[i] = ((self.preIssueBuff[i]))

        indices[4] = (self.preALUBuff[0])
        indices[5] = (self.preALUBuff[1])
        indices[6] = (self.postALUBuff[1])
        indices[7] = (self.preMemBuff[0])
        indices[8] = (self.preMemBuff[1])
        indices[9] = self.postMemBuff[1]

        for i in range(0,10):

            if indices[i] > -1:
                if instrName[indices[i]] in ['MOVZ', 'ADD', 'SUB', 'AND', 'OR', 'MUL']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR'+ str(self.arg3[indices[i]]) + ', R' + str(self.arg1[indices[i]]) + ', R' + str(self.arg2[indices[i]])+ ']'
                elif instrName[indices[i]] in ['SLL', 'SRL']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(self.arg1[indices[i]]) + ', R' + str(self.arg2[indices[i]]) + ', #' + str(self.arg3[indices[i]]) + ']'
                elif instrName[indices[i]] in ['BEQ', 'ADDI']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(self.arg2[indices[i]]) + ', R' + str(self.arg1[indices[i]]) + ', #' + str(self.arg3[indices[i]]) + ']'
                elif instrName[indices[i]] in ['SW', 'LW']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + '\tR' + str(self.arg2[indices[i]]) + ', ' + str(self.arg3[indices[i]]) + '(R' + str(self.arg1[indices[i]]) + ')'+ ']'
                elif instrName[indices[i]] == 'BLTZ':
                    formattedInstr[i] = '\t[' +  'BLTZ\tR' + str(self.arg1[indices[i]]) + ', #' + str(arg3[indices[i]]) + ']'
                elif instrName[indices[i]] == 'J':
                    formattedInstr[i] = '\t[' +  'J\t#' + str(self.arg1[indices[i]]) + ']'
                elif instrName[indices[i]] == 'JR':
                    formattedInstr[i] = '\t[' + 'JR\tR' + str(self.arg1[indices[i]])+ ']'
                elif instrName[indices[i]] in ['NOP', 'BREAK', 'Invalid Instruction']:
                    formattedInstr[i] = '\t[' + self.instrName[indices[i]] + ']'
            else: 
                formattedInstr[i] = ''

        pipelineFile.write('--------------------\n' 
            + 'Cycle:' + str(self.cycle)
            + '\n\nPre-Issue Buffer:\n'
            + '\tEntry 0:' + formattedInstr[0] + '\n'
            + '\tEntry 1:' + formattedInstr[1] + '\n'
            + '\tEntry 2:' + formattedInstr[2] + '\n'
            + '\tEntry 3:' + formattedInstr[3] + '\n'
            + 'Pre_ALU Queue:\n'
            + '\tEntry 0:' + formattedInstr[4] + '\n'
            + '\tEntry 1:' + formattedInstr[5] + '\n'
            + 'Post_ALU Queue:\n'
            + '\tEntry 0:' + formattedInstr[6] + '\n'
            + 'Pre_MEM Queue:\n'
            + '\tEntry 0:' + formattedInstr[7] + '\n'
            + '\tEntry 1:' + formattedInstr[8] + '\n'
            + 'Post_MEM Queue:\n'
            + '\tEntry 0:' + formattedInstr[9] + '\n')

        pipelineFile.write('\nRegisters' 
            + '\nR00:\t' + str(self.R[0]) + '\t' + str(self.R[1]) + '\t' + str(self.R[2]) + '\t' + str(self.R[3]) 
            + '\t' + str(self.R[4]) + '\t' + str(self.R[5]) + '\t' + str(self.R[6]) + '\t' + str(self.R[7])
            + '\nR08:\t' + str(self.R[8]) + '\t' + str(self.R[9]) + '\t' + str(self.R[10]) + '\t' + str(self.R[11]) 
            + '\t' + str(self.R[12]) + '\t' + str(self.R[13]) + '\t' + str(self.R[14]) + '\t' + str(self.R[15])
            + '\nR16:\t' + str(self.R[16]) + '\t' + str(self.R[17]) + '\t' + str(self.R[18]) + '\t' + str(self.R[19]) 
            + '\t' + str(self.R[20]) + '\t' + str(self.R[21]) + '\t' + str(self.R[22]) + '\t' + str(self.R[23])
            + '\nR24:\t' + str(self.R[24]) + '\t' + str(self.R[25]) + '\t' + str(self.R[26]) + '\t' + str(self.R[27]) 
            + '\t' + str(self.R[28]) + '\t' + str(self.R[29]) + '\t' + str(self.R[30]) + '\t' + str(self.R[31])
            + '\n')
            
        
        pipelineFile.write('\nCache\n')

        for i in range(4):
            pipelineFile.write('Set ' + str(i) +': LRU=' + str(self.cache.lruBit[i]) + '\n')

            for j in range(2):
                pipelineFile.write('\tEntry ' + str(j) + ':[('+ str(self.cache.cacheSet[i][j][0]) + ','
                    + str(self.cache.cacheSet[i][j][1]) + ','+ str(self.cache.cacheSet[i][j][2]) 
                    + ')<'+ str(self.cache.cacheSet[i][j][3]) + ',' + str(self.cache.cacheSet[i][j][4]) 
                    + '>]\n')

        pipelineFile.write('\nData')
        dataAddress = 96 + (self.numInstructions * 4)
        i = 0

        while i < len(self.memory):
            if( i % 8 == 0 and i == 0):
                pipelineFile.write('\n' + str(dataAddress) + ':' + str(self.memory[i])),
            elif( i % 8 == 0 and not i == 0):
                pipelineFile.write('\n' + str(dataAddress) + ':' + str(self.memory[i])),
            else: #not a multiple of 8
                pipelineFile.write('\t' + str(self.memory[i])),
            i += 1
            dataAddress += 4
        pipelineFile.write('\n')

    def isMemOp(self, index):
        if self.instrName[index] in ['LW', 'SW']:
            return True
        return False

    def getIndexOfMemAddress(self, wbAddr):
        return ((wbAddr - (96 + (4 * self.numInstructions)))/4)
      
    def run( self):
        go = True
        while go:
            self.WB.run()
            self.ALU.run()
            self.MEM.run()
            self.issue.run()
            go = self.fetch.run()

            if not go:
                self.cache.finalFlush()
            self.printState()
            self.cycle+=1
            

sim = simClass(instruction, opcode, memory, valid, address, arg1, arg2, arg3, numInstructions, 
    dest, src1, src2, instrName)
sim.run()

f.close()
disFile.close()
pipelineFile.close()


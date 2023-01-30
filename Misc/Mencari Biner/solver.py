from pwn import *

r = remote("167.71.212.18", 64896)

nums = [i for i in range(100)]

trying = 0
while True:
    mid_index = len(nums) //2
    
    r.sendline(str(nums[mid_index]).encode("utf8"))

    recv = r.recvline()

    if b"good job!!!" in recv:
        trying += 1
        print("SUCCESS, TRY", trying)
        nums = [i for i in range(100)]
        continue
    elif b"apah?" in recv:
        nums = nums[mid_index:]
    elif b"huh?" in recv:
        nums = nums[:mid_index]
    else:
        print(recv.decode("utf8"))
        break

r.close()
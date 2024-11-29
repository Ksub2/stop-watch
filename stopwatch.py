import time
print("Press Enter to start the stop watch")
print("press ctrl+C to stop ! ")
while True:
    try:
        input()
        start_time=time.time()
        print("Stopwatch started...")
    except:
        print("stopwatch stopped!!!")
        end_time=time.time()
        print("total time:",round(end_time - start_time,2),"seconds.")
        break

    
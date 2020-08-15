import psutil

def banner():
    print("""╔═╗┬─┐┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┬ ┬┌─┐┌─┐┌─┐┌┐┌┌┬┐┌─┐┬─┐
╠═╝├┬┘│ ││  │  ├┤ └─┐  ╚═╗│ │└─┐├─┘├┤ │││ ││├┤ ├┬┘
╩  ┴└─└─┘└─┘└─┘└─┘└─┘  ╚═╝└─┘└─┘┴  └─┘┘└┘─┴┘└─┘┴└─ 
             Coder By Rei-ken
            """)

def suspend():
    while True:
        pid=input("Suspend işlemi gerçekleştireceğiniz pencerenin PİD numarasını giriniz: ")
        procced=psutil.Process(int(pid))
        def error():
            print("Hatalı İşlem.")
        def resume():
            procced.resume()
            print("Uygulama kaldığı yerden devam ediyor.")
        def pause():
            procced.suspend()
            print("Duraklatıldı.")
        print("1]Suspend 2]Resume")
        secenek=input(" :")

        if(secenek=="1"):
            pause()
            devam=input("resume yapmak için 1 , çıkış için 2 yazınız.")
            if(devam=="1"):
                resume()
            elif(devam=="2"):
                exit()
            else:
                error()
        elif(secenek=="2"):
            resume()
        else:
            error()

banner()
suspend()
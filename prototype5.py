# Program Streak Tiktok
# Menghitung streak tiktok tiap teman/akun yang sudah ditambahkan sebelumnya
# KAMUS
#   hari, restored, i, N : int 
#   teman, chat_teman, chat, kirim , balas, balikkan_streak : str
#   teman, sum_streak, warna_api, hari_relatif : array [' '] of N
#   api : array
hari = 0
restored = 5
i = 0
api = ["kuning", "jingga", "merah", "pink", "ungu", "belum"]
N = int(input("Kamu ingin nambah berapa teman: "))
teman = [' ' for i in range(N)] 
for i in range (0,N):
    teman[i] = str(input(f'Kamu ingin namain teman {i+1} siapa: '))
    i = i +1
if i > 0:
    print("Daftar teman kamu:")
    for i in range(i):
        print(teman[i])
else:
    print("Kamu belum tambahkan temanmu")
sum_streak = [' ' for i in range(N)] 
for i in range (0, N):
    sum_streak[i] = 0
    i = i +1
warna_api = [' ' for i in range(N)]
hari_relatif = [' ' for i in range(N)]
selesai_chat = [False for i in range(N)]
waktu_kesempatan = [' ' for i in range(N)]
if i>0:
    print("Chat telah ditambahkan")
    kondisi_chat = True
    while kondisi_chat :
        hari = hari + 1
        print("hari ke:", hari)
        for i in range(0, N):
            hari_relatif[i] = hari
            selesai_chat[i] = False
            waktu_kesempatan[i] = 3
        teman_selesai = 0
        fitur_dm = True
        while fitur_dm:
            for i in range(0,N):
                if 3 <= sum_streak[i] < 10:
                    warna_api[i] = api[0]
                    break
                elif 10 <= sum_streak[i] < 30:
                    warna_api[i] = api[1]
                    break
                elif 30 <= sum_streak[i] < 100:
                    warna_api[i] = api[2]
                    break
                elif 100 <= sum_streak[i] < 200:
                    warna_api[i] = api[3]
                    break
                elif 200 <= sum_streak[i] :
                    warna_api[i] = api[4]
                    break
                elif 1 <= sum_streak[i] < 3:
                    warna_api[i]  = api[5]
                else:
                    warna_api[i] = api[5]
            chat_teman = str(input("Apakah kamu ingin chat teman kamu sekarang?(Ya atau Tidak): "))
            if chat_teman == "Ya":
                chat = str(input("Kamu ingin chat siapa: "))
                for i in range(0,N):
                    if chat == teman[i] and sum_streak[i] <= hari_relatif[i] - 1 and selesai_chat[i] == False:
                        print(f'Streakmu dengan {teman[i]} sekarang adalah {sum_streak[i]}')
                        kirim = str(input("Textbox: "))
                        balas = str(input(f'Apakah {teman[i]} membalas dalam 24 jam terakhir?(Ya atau Tidak): '))
                        if balas == "Ya":
                            selesai_chat[i] = True
                            sum_streak[i] = sum_streak[i] + 1
                            if sum_streak[i]%30!=0:
                                if 3 <= sum_streak[i] < 10:
                                    print(f"Wow!! selamat api kamu berwarna {api[0]}")
                                    break
                                elif 10 <= sum_streak[i] < 30:
                                    print(f"Wow!! selamat api kamu berwarna {api[1]}")
                                    break
                                elif 30 <= sum_streak[i] < 100:
                                    print(f"Wow!! selamat api kamu berwarna {api[2]}")
                                    break
                                elif 100 <= sum_streak[i] < 200:
                                    print(f"Wow!! selamat api kamu berwarna {api[3]}")
                                    break
                                elif 200 <= sum_streak[i] :
                                    print(f"Wow!! selamat api kamu berwarna {api[4]}")
                                    break
                                elif 1 <= sum_streak[i] < 3:
                                    print("Ayo terus ngobrol dengan teman kamu, apimu siap membara")
                                    break
                            else:
                                restored=5
                                if 3 <= sum_streak[i] < 10:
                                    print(f"Wow!! selamat apimu dengan {teman[i]} berwarna {api[0]}")
                                    break
                                elif 10 <= sum_streak[i] < 30:
                                    print(f"Wow!! selamat apimu dengan {teman[i]} berwarna {api[1]}")
                                    break
                                elif 30 <= sum_streak[i] < 100:
                                    print(f"Wow!! selamat apimu dengan {teman[i]} berwarna {api[2]}")
                                    break
                                elif 100 <= sum_streak[i] < 200:
                                    print(f"Wow!! selamat apimu dengan {teman[i]} berwarna {api[3]}")
                                    break
                                elif 200 <= sum_streak[i] :
                                    print(f"Wow!! selamat apimu dengan {teman[i]} berwarna {api[4]}")
                                    break
                                elif 1 <= sum_streak[i] < 3:
                                    print(f'Ayo terus ngobrol dengan {teman[i]}, apimu siap membara')
                                    break
                            teman_selesai = teman_selesai + 1    
                        else:
                            selesai_chat[i] = True
                            if sum_streak[i] >= 1:
                                print(f'Yah, {teman[i]} lupa balas chat kamu, api telah padam silahkan restored')
                                balikkan_streak = str(input("Apakah kamu ingin restored?(Ya atau Tidak): "))
                                if balikkan_streak == "Ya" and restored > 0:
                                    restored = restored - 1
                                    print("Sisa restored adalah", restored)
                                    sum_streak[i] = sum_streak[i]
                                    break
                                elif balikkan_streak == "Tidak" and restored > 0:
                                    print(f'Sayang sekali, streakmu dengan {teman[i]} putus')
                                    sum_streak[i] = 0
                                    break
                                else:
                                    print(f'Yah, restoredmu habis, streakmu dengan {teman[i]} putus deh')
                                    sum_streak[i] = 0
                                    break
                            else:
                                print(f'Yah, {teman[i]} tidak balas chat kamu, silahkan chat teman lain atau chat di hari berikutnya')
                                sum_streak[i] = 0
                                break 
                        teman_selesai = teman_selesai+1
                    elif chat == teman[i] and restored == restored and selesai_chat[i]==True:
                        print("Chat teman lain")
                        teman_selesai = teman_selesai-1
                        break
            else:
                for i in range (0,N):
                    if selesai_chat[i]==False:
                        if sum_streak[i] < 1:
                            print("Oke, cobalah untuk chat teman kamu yang lain")
                            teman_selesai = teman_selesai-1
                            break
                        elif waktu_kesempatan[i] > 0 and sum_streak[i] >= 1:
                            print(f'Apimu dengan {teman[i]} berwarna abu-abu sekarang, hati-hati nanti padam loh')
                            waktu_kesempatan[i] = waktu_kesempatan[i] - 1
                            print("sisa waktu:", waktu_kesempatan[i])
                            teman_selesai= teman_selesai-1
                            break
                        else:
                            if sum_streak[i] >= 1:
                                print(f'Yah, kamu lupa streak hari ini, apimu dengan {teman[i]} telah padam silahkan restored')
                                balikkan_streak = str(input("Apakah kamu ingin restored?(Ya atau Tidak): "))
                                selesai_chat[i] = True
                                if balikkan_streak == "Ya" and restored > 0:
                                    restored = restored - 1
                                    print("Sisa restored adalah", restored)
                                    break
                                elif balikkan_streak == "Tidak" and restored > 0:
                                    print(f'Sayang sekali, streakmu dengan {teman[i]} putus')
                                    sum_streak[i] = 0
                                    break
                                else:
                                    print(f'Yah, streakmu dengan {teman[i]} putus deh')
                                    sum_streak[i] = 0
                                    break
                            else:
                                print(f'Yah, kamu tidak balas chat {teman[i]}')
                                sum_streak[i] = 0
                                break           
            teman_selesai = teman_selesai + 1
            if teman_selesai == N:
                break
        for i in range(0,N):
            print(f'{teman[i]} streakmu sekarang: {sum_streak[i]}, apimu {warna_api[i]} membara')
else:   
    print("")

    
    
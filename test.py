# import os
# import subprocess
# from pydub import AudioSegment
# # path = os.path


# my_files = []
# peers_parent = []
# peers = []

# # index[13]
# for file_in_dir in os.scandir("dir_st"):
#     peers_parent.append(file_in_dir.name)


# for idx in range(len(peers_parent)):
#     if (peers_parent[idx] not in peers) and (len(peers) < 2):
#         peers.append(peers_parent[idx])

        # if str(peers_parent[idx]).startswith(peers_parent[idx][0:13]) == str(peers[0]).startswith(str(peers[0][0:13])):
        #     print("parent:",peers_parent[idx][-13:-1])
        #     print("child:",peers[0][-13:-1])
        #     if str(peers_parent[idx]).endswith(peers_parent[idx][-13:-1]) != str(peers[0]).endswith(peers[0][-13:-1]):
        #         print("there are not the same..", peers[0][-13:-1])



# print(peers)






            # print(peers_parent[idx] != peers[0])
            # peers.append(peers_parent[idx])
            # my_files.append(peers)
            # print(True)

            # pass
            # print(peers[peers_idex])
            # if str(peers_parent[idx]).startswith(peers_parent[idx][0:13]) == str(peers[peers_idex]).startswith(str(peers[peers_idex][0:13])) and str(peers_parent[idx]).endswith(peers_parent[idx][-13:-1]) != str(peers[0]).startswith(str(peers[peers_idex][-13:-1])):
                # peers.append(peers_parent[idx])









    # my_files.append(peers)
    # print("unique:", file.name[-13:-1])



# OMG
    # if (file.name not in peers) and (len(peers) < 2):
    #     peers.append(file.name)
    #     for i in range(len(peers)):
    #         print(peers[i])




            # if file.name.startswith(file.name[0:13]) == str(peers[0]).startswith(str(peers[0][0:13])) and file.name.endswith(file.name[-13:-1]) != str(peers[0]).startswith(str(peers[0][-13:-1])):
            #     pass
        #     peers.append(file.name)
        #     my_files.append(peers)
        #     print("peered...")

# print(my_files)





# if (os.path.isfile(audio_1) or os.path.isfile(audio_2)):
#     os.remove("./{:s}/{:s}".format(dir, audio_1))
#     os.remove("./{:s}/{:s}".format(dir, audio_2))
# else:
#     print("No such file in specified dir.")


from datetime import datetime

date = datetime.now()
# date_time = str(date).replace(':', '').replace('.', '').replace(' ', '')

print(date.date())

tr = '1-1674198613.1245_20230120T071016.987Z_08140262621.mp3'

# tr ="1-1674031236.15363_20230118T084041.565Z_09062145060.mp3"

ot = '1-1674217520.28287_20230120T122530.470Z_1_30019.mp3'

cv = '20230126T071315.272Z_1-001674717175.4_07032777268_112.mp3'

# print("{:s}_{:s}_{:s}{:s}_{:s}".format(str(tr[18:31]).replace('_', ''), ot[35:39], tr[0:13], ot[35:41], tr[35:]))

print(tr.split('_'))



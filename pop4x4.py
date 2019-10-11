#!/usr/bin/python

row_all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#row_all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

all00 = 0

plik = open("pop4x4.txt", "wb")
for a1 in row_all[0:41]:
 print a1
 for a2 in row_all[1:42]:
  if (a2 > a1):
   for a3 in row_all[2:43]:
    if (a3 > a2):
     for a4 in row_all[3:44]:
      if (a4 > a3):
       for a5 in row_all[4:45]:
        if (a5 > a4):
         for a6 in row_all[5:46]:
          if (a6 > a5):
           for a7 in row_all[6:47]:
            if (a7 > a6):
             for a8 in row_all[7:48]:
              if (a8 > a7):
               ttt = [a1, a2, a3, a4, a5, a6, a7, a8]
               all00 = all00 + 1
#               plik.write("\n" + str(ttt)
plik.close()
print all00

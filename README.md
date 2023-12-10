# ABOH23-Write-Up-OSINT-TH-Cypto

# OSINT

**Sorry, i dont remember the question title for OSINT D:**

**First Question that i get is**

![WhatsApp Image 2023-12-10 at 17 27 17_88efdee7](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/d7547050-ea59-4839-b6c4-a4e0f1387978)

Here's the picture given

Flag format ABOH23{Station_1,Station_2}

Use Google Lens to find details about the picture

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/bccd44b7-7702-4884-b3f5-6dafc1cc1dab)

If you see the number one, it's same with picture given, it says about 'Gold Line' and the place at Bangkok

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/6dc2a82e-5f58-491e-8e2a-baeb6463360c)

So, search the the place on Google Maps

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/351be077-caff-446d-9e7b-be802195539c)

There are 3 station on Golden Line:

- Krung Thon Buri/Krung Thonburi
- Charoen Nakhon
- Khlong San

The flag is ABOH23{Krung_Thon_Buri,Charoen_Nakhon}

**Move on to the next question**

Given the 2 youtube link

https://www.youtube.com/watch?v=QMlNLo74mOw

https://www.youtube.com/watch?v=Hs3LFwb8b7w

So there is similarity between two videos where it was the shooting place

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/aa37257d-8aef-4d6a-9007-0562b37ca434)
![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/1d8a7b81-00fe-442d-87b5-c8e07248ac3d)

So when you Google Lens for the picture from Future Perfect MV, you found this and choose that one

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/2d3649f6-1ddf-4189-ab50-4679e3c669a5)

After that, in the blog, there's say about a location which is Donga Land Transport Company, but to find the address you need to search the place in korean

So, take this picutre and go to Google Lens

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/3ee08ad8-1386-4ba4-8a84-72d7fc6354da)

Select the '동아 육운 창고' in the picture and choose the first link website

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/f7bc7a03-fedf-44c8-af85-0c45ef9cca62)

In the website, you can translate it into english and go to the website footer, there is the exact location address for the flag on the left

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/223ad77a-b002-47f3-abb3-49a64347a684)

But we need the full address, so, take the address and search it on google maps

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/c50e8b1b-2871-4186-aad1-f837895f3969)

Copy the address and follow the format

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/8e035290-8a20-4bce-a6a0-565991c27a4b)

The flag is ABOH23{1068_Poeun-daero_Mohyeon-eup_Cheoin-gu_Yongin-si_Gyeonggi-do_South_Korea}

# Threat Hunting

**Challenge 1**

So when you start and login the Windows Server, go to directory of System32

There are several unknown .exe files, one of them is Mcqqic24UJyU40JKdja0A.exe

The flag is ABOH{Mcqqic24UJyU40JKdja0A.exe}

**Challenge 2**

There is another .exe file and get the SHA256 by using command on Powershell

*Get-FileHash C:\Path\To\File.exe -Algorithm SHA256*

The flag is ABOH{2e1594cea1d8e012c709f3d71a4e57dcbc9d017b89f623822fc56c9f734eb491}

# Crypto

**Challenge1**

First we look at the file output.txt

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/70a10bb3-f632-41f0-8f1b-3f3eb172badc)

After that, we go to dcode RSA Decoder website, so there was the flag

![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/3d248168-4da9-414e-aeb9-ef09a5f852dd)

The flag is ABOH23{rocky0ubrr!}

**Challenge2**

We have a encrypt.py file so we can check that
![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/c7183d8b-704e-4d19-9b5e-54426fa32070)
![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/c5571ff1-46f9-485f-9a06-8558a0b0429e)
![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/e4420adf-d2fc-48ea-b522-ed666773edef)
![image](https://github.com/ZubayrYayYay/ABOH23-Write-Up-OSINT-TH-Cypto/assets/125542852/9e9d0322-8688-46a9-b766-4e08ae880452)







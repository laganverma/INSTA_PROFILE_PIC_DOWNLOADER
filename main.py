import instaloader

mod = instaloader.Instaloader()

a = input("Profile name : ")

mod.download_profile(a, profile_pic = True)


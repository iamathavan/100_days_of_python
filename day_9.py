logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
d={} 
con=True
while con:
    key=input("Enter your name: ")
    d[key]=int(input("Enter bid:$"))
    next=input("Are there any other bidders?type yes or no: ").lower()
    print("\n" * 50)
    if next=="no":
        con=False
maxbid=max(d.values())
key=[key for key,value in d.items() if value==maxbid]

print(f"The bid won by {key[0]} by bidding {maxbid}")

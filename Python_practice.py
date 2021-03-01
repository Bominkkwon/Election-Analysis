print("Hello World")

# counties = ['Arapahoe','Denver','Jefferson']
# if counties[1] == 'Denver':
#     print(counties[1])


# # temperature = int(input("what is the temp outside?"))
# # if temperature > 80:
# #     print("Turn on the AC.")
# # else:
# #     print("open the window")


# score = int(input("what is your test score"))
# if score >= 90:
#     print("your grade is an A")
# else:
#     if score >= 80:
#         print("your grade is a B")
#     else:
#         if score >=70:
#             print("your geade is C")
#         else:
#             if score >= 60:
#                 print("ur grade is a D")
#             else:
#                 print("u r failing")

# counties = ['Arapahoe','Denver','Jefferson']
# if 'El Paso' in counties:
#     print("El paso is in the list of counties.")
# else:
#     print('El Paso is not the list of counties')

# if 'Arapahoe' in counties and 'El paso' in counties:
#     print("ara and el are in the list")
# else:
#     print("they are not in the list")

# count = 7
# while count < 1:
#     print("Hello World")

# counties = ['Arapahoe','Denver','Jefferson']
# for county in counties:
#     print(county)

# numbers = [0,1,2,3,4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(i)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for i in range(len(voting_data)):

#       print(voting_data[i])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county,votes in counties_dict.items():
#     county_data = (
#         f"{county} county has {(votes):,} registered votes")
       
#     print(county_data)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for each_county in voting_data:
#         print(f'{each_county["county"]} county has {each_county["registered_voters"]:,} registered votes')

import datetime
now = datetime.datetime.now()
print("the time right now is", now)













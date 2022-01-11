import builtins


print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, "county has ", voters, "registered voters")

voting_data = [{"county":"Arapahoe", "registered voters": 422829}, {"county": "Denver", "registered voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)

candidate_votes = int(input(3345))
total_votes = int(input(123123))
message_to_candidate = (f'You received {candidate_votes:,} number of votes.' f'The total nunber of votes in the election was {total_votes:,}.' f'You receieved {candidate_votes / total_votes *100:.2f}% of the total votes')
print(message_to_candidate)

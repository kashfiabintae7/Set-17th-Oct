
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

intersection = set1.intersection(set2)

total_guests = list(intersection)

print('Total guests to be invited in the party are: ', len(total_guests))
print('Guest List: ', total_guests)
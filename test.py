l= input() # User Input
userList = l.split() # Split the input into str list
max=0
sum=0
for i in range (len(userList)):
	if i%2==0:
		sum+=int(userList[i])
	else:
		sum-=int(userList[i])
	if sum>max:
		max=sum# To find the peak and design matrix parameter

a=0		
for i in userList:
	a+=int(i)# sum of all entries to find the number of columns of the matrix

c = [ [ " " for i in range(a+10) ] for j in range(max+10) ] 


temp1=max+2 # Arbitrary value to define the structure of the peak
temp2=0
xpeak_coord=0# Coordinates for the highest peak
ypeak_coord=0

max=0
sum=0

for i in range (len(userList)):	
	if i%2==0:
		sum+=int(userList[i])
		for d in range(int(userList[i])):	
			# If even index the slope is up
			temp2+=1
			c[temp1][temp2]='/'
			temp1-=1	
	else:
		sum-=int(userList[i])
		for d in range(int(userList[i])):
			# If odd index slope is down
			temp1+=1
			temp2+=1
			c[temp1][temp2]='\ '
			#temp2+=1
			#temp1+=1
		
	if sum>max:
		max=sum
		xpeak_coord=temp1# Update peak value
		ypeak_coord=temp2
			

#Design for man on the peak
c[xpeak_coord][ypeak_coord]= "< >"
c[xpeak_coord-1][ypeak_coord]= "/|\ "
c[xpeak_coord-2][ypeak_coord]= " o "

# Print the final graph
for i in range(max+3):
	for j in range(a):
		print(c[i][j],end=" ")
	print()




# def inverse(n):
#     res = 0
#     while n > 0:
#         a = n % 10
#         res = res * 10 + a
#         n = n // 10
#     return res
#
# vorodi=int(input())
# num=inverse(vorodi)+1
# newnum=num
# counter=0
# while newnum>0 :
#     newnum=newnum//10
#     counter+=1
#
# print(str(inverse(num)).zfill(counter))
# sec pro
# n=int(input())
# arr=[]
# for i in range(n):
#     a=[]
#     for j in range(n):
#         a.append(int(input(f"satr {i} va sotoon {j}")))
#     arr.append(a)
# counter=0
# breaked = False
# for i in range(n):
#     for j in range(n):
#         if arr[i][j]==3:
#             breaked=True
#             break
#         elif arr[i][j]==1:
#
#             counter+=1
#             continue
#         elif arr[i][j]==2:
#             counter+=1
#             j=j
#             next=True
#             break
#         else:
#             print('wrong')
#     if breaked:
#         break
#     if next:
#         continue
#
#
#
# print(counter)


# n= int(input())

# for i in range(n):
#
#
#     for j in range(n-i):
#         if i == 0 and j==0 :
#             print(' ',end='')
#             continue
#         print('*',end='')
#     for j in range(i):
#         print(' ',end='')
#     for j in range(i):
#         print(' ',end='')
#     for j in range(n-i):
#         if i == 0 and j == n-1:
#             print(' ', end='')
#             continue
#         print('*',end='')
#     print()
# for i in range(2,n+1):
#    for j in range(i):
#        if i == n and j == 0:
#            print(' ', end='')
#            continue
#        print('*',end='')
#    for j in range(n-i):
#        print(' ',end='')
#    for j in range(n-i):
#        print(' ', end='')
#    for j in range(i):
#        if i == n and j == n - 1:
#            print(' ', end='')
#            continue
#        print('*', end='')
#    print()


# n=int(input())
# azla = int(pow(2, n / 2 + 2) - 1)
# arr=[]
# for i in range(azla):
#     arr.append([])
#     for j in range(azla):
#         arr[i].append('.')
# while n>0:
#     nazla=int(pow(2, n / 2 + 2) - 1)
#     if n%2==0:
#         for i in range(nazla):
#             for j in range(nazla):
#                 if (i == 0 or j == 0) or (i == nazla - 1 or j == nazla - 1):
#                     arr[i][j] = '#'
#     else:
#         mid=
#         for i in range(mid):
#             for j in range(mid):
#                 if i+j==
#
#     n-=
# a='abcfg'
# b='abdefg'
# for i in a:
#     if i in b:
#         print(i)



# row=int(input())
# col=int(input())
# area=[]
# gholle="No Gholle Found"
#
# for i in range(row):
#     area.append([])
#     for j in range(col):
#         area[i].append(int(input()))
# for i in range(1,row+1):
#     if i == 1 or i == row:
#         continue
#     for j in range(1,col+1):
#          if j==1 or j==col:
#             continue
#          # print(area[i-1][j-1])
#          max_nei=max(area[i-1][j-2] ,area[i-1][j],area[i-2][j-1],area[i-2][j-2],area[i-2][j],area[i][j-2],area[i][j-1],area[i][j])
#          if area[i-1][j-1]>max_nei:
#              gholle=[i,j]
# for i in gholle:
#     print(i,end=' ')


# import math
# import time
# q=int(input())
# zojha=[]
# for i in range(q):
#     zojha.append([])
#     for j in range(2):
#         zojha[i].append(int(input()))
# maxs=[]
# for i in zojha:
#     maxs.append(i[1])
# maxnum=int(max(maxs))
# def primenum(num):
#
#     prime = [True for i in range(num + 1)]
#
#     p = 2
#     while (p * p <= num):
#
#         if (prime[p] == True):
#
#
#             for i in range(p * p, num + 1, p):
#                 prime[i] = False
#         p += 1
#         prime[0]=False
#         prime[1]=False
#
#
#     return prime
#
# primeslist=primenum(maxnum)
# print(primeslist)
#
#
# for zoj in zojha:
#    templist=primeslist[zoj[0]:zoj[1]+1]
#    counter=0
#    for i in templist:
#        if i==True:
#            counter+=1
#    print(counter)
# finding prime number




nodes=int(input())
routenums=int(input())
routes=[]
def graphcounter(graph):
    visited=set()
    count=0
    for node in graph:
        if moveingraph(graph,node,visited):
            count+=1
    print(count)



def moveingraph(graph,node,visited):
    if node in visited:
        return False
    visited.add(node)
    for nei in graph[node]:
        moveingraph(graph,nei,visited)
    return True


for i in range(routenums):
    routes.append([])
    for j in range(2):
        routes[i].append(int(input()))

graph={}
for node in range(1,nodes+1):
    graph[node]=[]
for a,b in routes:
    graph[a].append(b)
    graph[b].append(a)
graphcounter(graph)



# class solution:
#     def countcomp(self,n,edges):
#         if n==1:
#             return 1
#         comps=0
#         graph={node:[] for node in range(n)}
#         for node1,node2 in edges:
#             graph[node1].append(node2)
#             gra




























































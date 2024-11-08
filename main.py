setx= {"green", "blue"}
sety = {"blue", "yellow"}
print("original set elements:")
print(setx)
print(sety)
print("\nInteraction of two said sets:")
setz = setz.intersection(sety)
print(setz)

setz=setx.union(sety)
print(setz)

setz=setx.diffenrence(sety)
print(setz)

setz=setx.symmetric_differences(sety)
print(setz)
from time import perf_counter, sleep


def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


file = open("prime numbers.txt", "w")

max = int(input("Bis zu welcher Stelle möchten Sie die Primzahlen ausgegeben bekommen? "))
primeCount = 0
start = perf_counter()

firstline = True
for i in range(2, max):
    if isPrime(i):
        if firstline:
            file.write(str(i))
            firstline = False
            primeCount += 1
        else:
            file.write(",\n" + str(i))
            primeCount += 1

end = perf_counter()

file.write(".\nInsgesamt ausgegebene Primzahlen: " + str(primeCount) + " oder " + str(
    primeCount / max * 100) + "% der Zahlen.")
file.write("\nBenötigte Zeit: " + str(end - start) + " Sekunden oder " + str(
    primeCount / (end - start)) + " Primzahlen pro Sekunde.")
file.close()

print(
    "Insgesamt ausgegebene Primzahlen: " + str(primeCount) + " oder %.2f" % (primeCount / max * 100) + "% der Zahlen.")
print("Benötigte Zeit: %.2f" % (end - start) + " Sekunden oder %.2f" % (
            primeCount / (end - start)) + " Primzahlen pro Sekunde.")

sleep(15)

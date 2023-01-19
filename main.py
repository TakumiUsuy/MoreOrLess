import random as rd
from data import people

star_1 = {}
star_2 = {}
score = 0


def choose():
    global star_1, star_2
    st_1 = rd.randint(0, len(people) - 1)
    st_2 = rd.randint(0, len(people) - 1)
    star_1 = people[st_1]
    star_2 = people[st_2]
    people.pop(st_1 and st_2)


choose()


def game():
    def keys_of(dic):
        return list(dic.keys())

    def naming():
        print(f"Compare A: {star_1[keys_of(star_1)[0]]}, "
              f"{star_1[keys_of(star_1)[2]]}, from {star_1[keys_of(star_1)[3]]}.")
        print(f"Against B: {star_2[keys_of(star_2)[0]]}, "
              f"{star_2[keys_of(star_2)[2]]}, from {star_2[keys_of(star_2)[3]]}.")

    naming()

    def follow(acc):
        return acc[keys_of(star_1)[1]]

    def compare():
        a = follow(star_1)
        b = follow(star_2)
        if a > b:
            return 'a'
        elif b > a:
            return 'b'

    score = 0

    def checker():
        global score, star_1, star_2
        if input("Who has more followers? Type 'A' or 'B': ").lower() == compare():
            score += 1
            print(f"You're right! Current score: {score}.")
            if compare() == 'a':
                st_2 = rd.randint(0, len(people) - 1)
                star_2 = people[st_2]
                people.pop(st_2)
            else:
                star_1 = star_2
                st_2 = rd.randint(0, len(people) - 1)
                star_2 = people[st_2]
                people.pop(st_2)
            game()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")

    checker()


game()

import pygame
import random
from tkinter import *
root = Tk()
root.geometry('300x300')
root.title('Madlib Generator')
Label(root, text= "Madlib Generator \n 3 Fun Madlibs!", font = "arial 20 bold").pack()
Label(root, text= "Choose your Madlib", font = "arial 15 bold").place(x=50, y=80)

def madlib1():

    animals = input("Enter an animal: ")
    food = input("Enter a food: ")
    clothing = input("Enter a piece of clothing: ")
    things = input("Enter a thing: ")
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food: ")
    job = input("Enter a job: ")
    print(f"Once upon a time there was a {animals} named {name}. {name} lived in a {place} and loved to {verb} and eat {food}. One day, {name} got laid off from their job as a {job} and had to find a new one. They found a job at a restaurant and had to wear {clothing} while they worked. One day, they found a {things} in the restaurant and it made them want to quit. But they needed the money, so they stayed and continued to work hard. Eventually, they got promoted and lived happily ever after.")

def madlib2():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    name = input("Enter a name: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    food = input("Enter a food: ")
    print(f"Today I ran into my friend {name} at the {place}. We were both wearing {adjective} clothes and we decided to {verb} together. We had so much fun and we even saw a {adjective2} {animal} eating some {food}. It was a great day!")

def madlib3():   
    color = input("Enter a color: ")
    noun = input("Enter a noun: ")
    adverb = input("Enter an adverb: ")
    verb = input("Enter a verb: ")
    name = input("Enter a name: ")
    thing = input("Enter a thing: ")
    monster = input("Enter a monster: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")
    time of day = input("Enter a time of day: ")
    print(f"One dark and stormy {time of day}, {name} was walking through the {place} on their way home from work. They were feeling {emotion} and wanted to go home and sleep. Suddenly, they heard a loud noise and saw a {monster} coming towards them. They were so scared that they started to {verb} {adverb}. They ran as fast as they could and eventually found a {thing} to hide behind. The {monster} couldn't find them and eventually went away. {name} was so relieved and grateful to be alive. They went home and slept soundly, dreaming of a world without {monster}s.)")


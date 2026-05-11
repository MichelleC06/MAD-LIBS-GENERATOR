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

    





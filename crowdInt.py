from random import uniform
import matplotlib.pyplot as plt

while True:
    print("Type '-1' to stop the program")
    try:
        # was is the correct solution?
        solution = float(input("What is the correct answer?: "))
        # stop program if input is '-1'
        if solution == -1:
            break
        # 1: minimum = correct answer - 100% * correct answer
        # 2: minimum = correct answer - 90% * correct answer
        # etc.
        competence = float(input("How competent is the audience? (1-10): "))
        # number of people partizipating
        crowdSize = int(input("How big is the audience?: "))

        # depends on comeptence; ranges from 10% to 100%
        factor = (11-competence)/100

        # setting ranges for badest guesses
        minLim = solution - factor * solution
        maxLim = solution + factor * solution

        guesses = list()
        persons = list()
        sumGuess = 0
        # each persons make his or her guess
        # guesses are saved to plot them later
        for i in range(crowdSize):
            guess = uniform(minLim,maxLim)
            guesses.append(guess)
            persons.append(i+1)
            sumGuess += guess

        # calculation of average guess
        avg = round(sumGuess/crowdSize,2)
        print(f"The average guess was: {avg}")

        # necessary to plot the solution and average later
        solutions = list()
        avgs = list()
        for i in range(crowdSize):
            solutions.append(solution)
            avgs.append(avg)

        # scatter plot of all guesses
        plt.scatter(persons,guesses,color='blue')
        # plot of the solution as a green line
        plt.plot(persons,solutions,color='green')
        # plot of the average guess as a red line
        plt.plot(persons,avgs,color='red')
        plt.xlabel('Persons')
        plt.ylabel('Guesses')
        # showing average value in title
        plt.title(f"Average: {avg}")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
        print("Please try again!")

    
    

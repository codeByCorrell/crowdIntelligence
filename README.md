# Python Simulation Crowd Intelligence
The basic idea of the program is to simulate crowd intelligence by simulating guesses of a crowd dependent on their competence and plotting the results afterwards.<br><br>
The program starts with the following three prompts. First of all it will ask you for the correct answer of the question, that the crowd tries to guess.
Thereafter you can set the competence of the crowd, which ranges from 1 (least competent) to 10 (most competent). Finally you'll have to set the size of the crowd.<br><br> 
The program will use the correct answer and the competence factor to calculate the range of possible guesses. If the competence is set to 1, then the lowest possible guess will be
```lowest possible guess = correct answer - 100% * correct answer``` and the maximum ```highest possible guess = correct answer + 100% * correct answer```. 
If the competence is set to 2 it will be ```lowest possible guess = correct answer - 90% * correct answer``` and ```lowest possible guess = correct answer + 90% * correct answer```
The range of possible answers will become smaller and smaller until the competence of 10 where the lowest and highest possible guesses will be ```lowest possible guess = correct answer - 10% * correct answer```
and ```lowest possible guess = correct answer + 10% * correct answer```<br><br>Within this intervall the program will create a random guess for each crowd member.
Finally the average of all guesses is calculated and the results are plotted. The plot will contain all guesses (blue dots), the correct answer (green line) 
as well as the average of all guesses (red line). An example of such a plot is shown below. Here the correct answer was 85. 30 people were guessing and the competence was set to 5.<br><br>
![output](https://github.com/user-attachments/assets/5812dbd2-fbc6-4fe5-b646-1b32512a4a20)
## Requirements
* Python3
* matplotlib : ```pip install matplotlib```

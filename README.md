# Internet Ping Test

## About and Background

This code pings google.com and reports on how much time passes in milliseconds between the time the request is sent and response is recieved. Upon running the program, it requests a user input for any comments you'd like to leave about the current test. This is intended to note what variables you are changing for this specific test. Based on what experiment you wish to run, you may want to modify the code to get accurate results. This can include what file you wish to save to and if you want to report on all responses or only those above a certain threshold. See comments in the code to determine where to change these.

I created this code to test if the reason Splatoon 3 internet disconnections, or Nintendo Switch Online disconnections, are happening on my network are because of ping spikes. Unfortunately, it appears that sometimes lag or disconnects happen when the ping spikes but other times the game disconnects while the ping is steady. Because of this, I cannot conclusively determine anything about the internet disconnections. I also don't have any baseline data from when Splatoon 3 wasn't disconnecting to determine if the internet typically has ping spikes or if this is a new issue.

## Example Usage

In the sample file, experiment1.xlsx, two trials were run for five minutes each. One where no devices were actively on the network (devices were still connected running in the background), and another where one Nintendo Switch is connected and playing Splatoon 3. The data from every request is exported to excel, where I manually reported on the means and variance of the two samples. The data is approximately normal since we take a large amount of samples with a continous distribution. I tested the null hypothesis pictured below

<img src="https://github.com/user-attachments/assets/b31e925c-8b0f-48c4-8997-50867822dd3a" style="width:70%; height:auto;">

Because of our conclusions we can determine that Splatoon 3 has a significant impact on the latency of the network for this trial. This makes sense because the program sends a new request as soon as the previous one is recieved. For the base trial, 1636 pings are recorded but while Splatoon 3 is running only 1078 are. This alone implies that the Splatoon 3 trial has a longer average time between request and response. 

However, since the internet being tested is shared Fiber Optics, it is possible that different households activity could skew results. It is also possible that the current internet problem is the reason the Splatoon 3 causes ping spikes. For a definite answer, multiple trials would need to be performed.

Once the internet issue is resolved, I will run some more tests and save the baseline data to compare against any future problems.


# Internet Ping Test

This code pings google.com and reports on how much time passes in milliseconds between the time the request is sent, and response is received. Upon running the program, it requests user input for any comments about the current test. This is intended to note what variables you are changing for this specific test. Based on what experiment you wish to run, you may want to modify the code to get accurate results. This can include what file you wish to save to and if you want to report on all responses or only those above a certain threshold. See comments in the code to determine where to change these values.

## Background

I created this code to test if the reason for frequent internet disconnections on Nintendo Switch is because of ping spikes. I couldn't conclusively determine if ping spikes were the cause for these disconnections, because the time where the console lost connection and the time that the ping spiked appear to not correlate. The ping would spike and the console would remain connected in some situations, in others it would spike and the console would lose connection, and in others the ping would be stable and the console would lose connection. However, this program did detect that spikes were more frequent and worse while Splatoon 3 was running.

## Example Usage

In the sample file, experiment1.xlsx, two trials were run for five minutes each back-to-back. In the first trial no devices were actively on the network (devices were still connected running in the background), and in the second one Nintendo Switch is connected and playing Splatoon 3. The data from every request is exported to excel, where I manually reported on the means and variance of the two samples. The data is approximately normal since we take a large number of samples with a continuous distribution. I tested the null hypothesis pictured below.

<img src="https://github.com/user-attachments/assets/b31e925c-8b0f-48c4-8997-50867822dd3a" style="width:70%; height:auto;">

Because of our conclusions we can determine that Splatoon 3 has a significant impact on the latency of the network for this trial. This makes sense because the program sends a new request as soon as the previous one is received. For the base trial, 1636 pings are recorded but while Splatoon 3 is running only 1078 are. This alone implies that the Splatoon 3 trial has a longer average time between request and response.  

However, since the internet being tested is shared Fiber Optics, it is possible that different household’s activity could skew results. It is also possible that the current internet problem is the reason Splatoon 3 causes ping spikes. For a definite answer, multiple trials would need to be performed, ideally under various conditions.

Once the internet issue on my network is resolved and connecting to a Nintendo Switch doesn't result in frequent disconnections, I will run more experiments on the correlations between Splatoon 3 and internet ping.
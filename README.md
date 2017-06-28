
# Differences in this library compared to others
  * We don't use conflicting pins.  We use software PWM for the servo and we use the SPI buss for the LED instead of using the 2 default PWM ports that are used for left and right audio.
		* We use analog audio to a speaker and use a different microphone than the small micro one everyone uses.  It has significantly better pickup for the cost difference.

# IBM's TJBot code rewritten in Python.

  * Things we want to be able to do in python:  
  * Speech to text, preferably more live than waiting for no sound to process, but whatever  
  * Again need to figure out how to add some keywords to his vocabulary  
  * Function waitforsomething(resetafter)   
  * Maybe if it keeps hearing something after a while it says idk how to help  
  * Text to speech, make sure you can do the character inflection and verbal tone stuff with taht one female voice.  
    * Function speak(text) maybe speak(text, emotion)  
  * Conversation, send text to the conversation module and have it return a string, possibly with inflection or some kind of string at the beginning [wave] where [] denotes a command and the inside is a command that TJ bot will process and do and then remove it before it speaks it or something.  
    * Function sendconversation(conversation), will wait for a response  
  * Tone analysis, send the text from speech to text through the tone to add some context for the conversation part.  Figure out how    to use the context stuff in teh conversation stuff.  
    * Function analyzetone(text), returns the emotion array  
    * Function analyzetonesimple(text), returns the highest option. Ex “sad”  
  * This Personality thing, no idea what it is.  

## Servo  
  Function wave(duration) or wave(count)  
  Function setangle(angle) or setangle(angle, speed)  
  Function up(), down(), forward() ---> just sends an angle to the set angle function  
  Function stop()  


## LED  
  Function setcolor(r,g,b) or setcolor(hex) or setcolor(color)  
  Function playsequence(sequence)  
  Sequence is a list of actions  
  A sequence has a repeat infinite, repeat count options   
  An action for the LED has a color and a duration  
  Function rainbow(speed) → does stuff with colors  
  Function strobe(speed) → strobes white at the speed  
  Function stop()  


## Music  
  Function playmusic(sound file)  
  Function volup(), voldown(), volmute()  
  Function pause(), stop(), restart()  


## Camera  
  Take a picture and just show it on the screen  
  Show a live video stream  


```
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM$7777OMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMM77777I777777778MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMM77777I$$$????I?II777I77ONMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMN777777$$$$$$?????????I???7777I777NMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMN7I7777$$$$$$$$?$7?I??????????I????I7777II7DMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMO7I7777$$$$$$$$Z???$$$MMMMMO??????????????77777I$ZMMMMMMMMMMMMMM
MMMMMMMMMMMMM$7I777$$$$$$$$OMMMZ???$$$MMMMMMMMMMMN$??I?7I777I$$$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM??II77777777OMMMMMMZ???$$$MMMMMMMMMMMMMM7I7777$$$$$$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM?????I???II7777778NZ???$$$MMMMMMMMMMN7777I7$$$$$$$7$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM????????????I???IIII???$7$MMMMMMM8I7777$$$$$$$$$7??$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I???????????????????$$$777IZI777I$$$$$$$$$DMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$$MMMMO????????????$$$I??I777$$$$$$$7$MMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMN7II???$$$??????$$$$$7ZMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$I?????$$$OMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MMI???$$MMMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MM????$$MMMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MM????$$MMMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MM????$$MMMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MM????$$MMMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MM????$$MMMMMMMMMMMMMO???$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$$MM????$$MMMMMMMMMMMMMO??I$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMMMMZ???$$78M??I?$$MMMMMMMMMMMMMO??I$$ZMMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMMMMOI777I7?I777I7II7$MMMMMMMMMMMMMO??I$$$MMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMMMMO77I7I7$$$????I?III777I7778MMMMMMMO???$$$MMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7MMMMZ7777I$$$$$$$???????????IIIII7II77IZDO???$$$MMMMMMMMMMMMMM
MMMMMMMMMMMM???I$7N777777$$$$$$$$8MMMNZ?????????????????I77I???$$$MMMMMMMMMMMMMM
MMMMMMMMMMMM???I$$7777$$$$$$$$DMMMMMMMMM???I$II???????????7777?$$$MMMMMMMMMMMMMM
MMMMMMMMMMMM???I7$$$$$$$$$$MMMMMMMMMMMMM???I$$MMMMMZ??II777I7$$$$$MMMMMMMMMMMMMM
MMMMMMMMMMMM????II??????NMMMMMMMMMMMMMMM???I$$MMMMMOI777I$$$$$$$7OMMMMMMMMMMMMMM
MMMMMMMMMMMM????????I??I??????ZMMMMMMMMM???I$$MM$I777I$$$$$$$$NMMMMMMMMMMMMMMMMM
MMMMMMMMMMMM????????????????????????IOMMI??I$$I7777$$$$$$$$MMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNI??I??????????????I??I???I$$I7$$$$$$$$MMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMN7??????????????????I$$$$$$$7ZMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM8II???I??????I$$$$$8MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM8I????I$$MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMM .D     .MMMMMMMM,     ,MMMMMM  M,     +MMMMMMMM.     ~MMMMO .MMMMMM  NMMMM
MMMMM   NMMM8  DMMMM$ .8MMMD. ZMMMM   ~MMMM? .MMMMM, .MMMM=  MMMM$  MMMM  MMMMMM
MMMMM  MMMMMM+  MMMM  MMMMMMM  MMMM  IMMMMMM8 .MMM~ ,MMMMMMM  MMMMO..MM  MMMMMMM
MMMMM  MMMMMMN  MMM~ ZMMMMMMM:  MMM  MMMMMMMM  MMM  MMMMMMMM  NMMMMD .. MMMMMMMM
MMMMM  MMMMMMN  MMM. MMMMMMMMZ  MMM  MMMMMMMM. NMM  MMMMMMMM  8MMMMMI  DMMMMMMMM
MMMMM  MMMMMMN  MMM: 8MMMMMMM=  MMM  MMMMMMMM  MMM. MMMMMMMM  NMMMM? ~. DMMMMMMM
MMMMM  MMMMMMN  MMMM  MMMMMMM. MMMM  ZMMMMMM8  MMM~  MMMMMMM  MMMM:..MM  NMMMMMM
MMMMM  MMMMMMN  MMMMI  OMMMM. ZMMMM   ,MMMM:  MMMMM...MMMM,  MMMM   MMMM .ZMMMMM
MMMMM  MMMMMMN  MMMMMM.  .   MMMMMM .M. ..  ~MMMMMMMM   .  ,MMMM. =MMMMMM. ,MMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
```

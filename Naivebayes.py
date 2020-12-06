# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:06:44 2020

@author: asus
"""
import pandas as pd
import pythainlp as nlp
#twt_text = 'อาจารย์ไม่เห็นใจผมเลย ไม่อยากทำแล้ว อาจารย์ก็ยังให้ผมทำอยู่ดี'

class Naivebayes:
    def __init__(twt_text):
        print('fffffffff')
        data = pd.read_csv(r'C:\Users\61050192\Desktop\io_project\Word_io_contingency.csv')
        w = nlp.word_tokenize(twt_text,engine='newmm',keep_whitespace=False)
        prob_Y = float(0.49561973)
        prob_N = float(0.50438027)
        for i in range(len(w)):
            IsNotFound = True
            for j in range(len(data.Word)):
                if(data.Word[j]==w[i]):
                    print(data.Word[j])
                    prob_Y = prob_Y * data.prob_yes[i]
                    prob_N = prob_N * data.prob_no[i]
                    print(prob_Y,prob_N)
                    IsNotFound = False
                    break
                elif(data.Word[j]!=w[i]):
                    pass
            if(IsNotFound):
                prob_Y = prob_Y * float(data.prob_yes[len(data.Word)-2])
                prob_N = prob_N * float(data.prob_no[len(data.Word)-2])
        print(w)
        ans = ''
        isIO = True
        if(prob_Y > prob_N):
            ans = "Yes this tweet is IO"
            isIO = True
        else:
            ans = "No this tweet isn't IO"
            isIO = False
        print(ans)
        #print(float(prob_Y))
        #(float(prob_N))
        return ans
        
#predict = Naivebayes.init(twt_text)
if __name__ == "__main__":
    __init__()
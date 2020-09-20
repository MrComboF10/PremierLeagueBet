# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:45:19 2020

@author: supertommc
"""

import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

print(pd.__version__)

class NN:
    
    def __init__(self, n_outputs):
        self.model = keras.Sequential([
            keras.layers.Dense(38, activation="relu", name="Input", input_shape=[38]),
            keras.layers.Dense(18, activation='relu', name="Hidden1"),
            keras.layers.Dense(9, activation='relu', name="Hidden2"),
            keras.layers.Dense(n_outputs, activation='softmax', name="Output")
        ])
        self.model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
        
    def get_data(self):
        train = pd.read_csv("training_set_hda.csv", header=0)
        test = pd.read_csv("testing_set_hda.csv", header=0)
        sim = pd.read_csv("sim_test_hda.csv", header=0)
        y_train = train.pop('RES')
        y_test = test.pop('RES')
        y_sim = sim.pop('RES')
        
        train.pop('HT')
        train.pop('AT')
        test.pop('HT')
        test.pop('AT')
        self.home_teams = sim.pop('HT')
        self.away_teams = sim.pop('AT')
        
        train_data = train.to_numpy()
        self.train_data = train_data/100.0
        test_data = test.to_numpy()
        sim_data = sim.to_numpy()
        self.sim_data = sim_data/100.0
        self.test_data = test_data/100.0
        self.train_labels = y_train.to_numpy()
        self.test_labels = y_test.to_numpy()
        self.sim_labels = y_sim.to_numpy()
        
        odds_data_temp = pd.read_csv('PL1920Odds.csv')
        self.odds_data = pd.concat([odds_data_temp.pop(x) for x in ['HT', 'AT', 'FTHO', 'FTDO', 'FTAO']], axis=1).to_numpy()
    
    def get_data_2(self):
        train = pd.read_csv("training_set_ou.csv", header=0)
        test = pd.read_csv("testing_set_ou.csv", header=0)
        sim = pd.read_csv("sim_test_ou.csv", header=0)
        y_train = train.pop('RES')
        y_test = test.pop('RES')
        y_sim = sim.pop('RES')
        
        train.pop('HT')
        train.pop('AT')
        test.pop('HT')
        test.pop('AT')
        self.home_teams = sim.pop('HT')
        self.away_teams = sim.pop('AT')
        
        train_data = train.to_numpy()
        self.train_data = train_data/100.0
        test_data = test.to_numpy()
        sim_data = sim.to_numpy()
        self.sim_data = sim_data/100.0
        self.test_data = test_data/100.0
        self.train_labels = y_train.to_numpy()
        self.test_labels = y_test.to_numpy()
        self.sim_labels = y_sim.to_numpy()
        
        odds_data_temp = pd.read_csv('PL1920Odds.csv')
        self.odds_data = pd.concat([odds_data_temp.pop(x) for x in ['HT', 'AT', 'FTO 2.5', 'FTU 2.5']], axis=1).to_numpy()   
    
    def check_team_names_integrity(self):
        
        odds_ht = [x[0] for x in self.odds_data]
        odds_at = [x[1] for x in self.odds_data]

        print(np.unique(self.home_teams) == np.unique(odds_ht))
        print(np.unique(self.away_teams) == np.unique(odds_at))
        
    def train_model(self, epochs_to_train): # train_data and train_labels are numpy arrays
            self.model.fit(self.train_data, self.train_labels, epochs=epochs_to_train)
        
    def evaluate_model(self):
        test_loss, test_acc = self.model.evaluate(self.test_data,  self.test_labels, verbose=1) 
    
        print('Test Loss:', test_loss)
        print('Test accuracy:', test_acc)
        
        return test_acc
        
    def save_model(self, path):
        self.model.save(path)
        
    def load_model(self, path):
        self.model = keras.models.load_model(path)
    
    def predict_full(self):
        predictions = self.model.predict(self.test_data)
        return predictions
        
    def predict_single(self, game):
        prediction = self.model.predict(np.array([game]))
        return prediction[0]
    
    def find_game(self, ht, at, hts, ats):
        for i in range(len(hts)):
            if ht == hts[i] and at == ats[i]:
                return i
        return -1


    def order_games(self):

        self.ordered_sim_games = []
        self.ordered_sim_labels = []

        odds_data_list = self.odds_data.tolist()

        for i in range(len(odds_data_list)):

            ht = odds_data_list[i][0]
            at = odds_data_list[i][1]

            idx = self.find_game(ht, at, self.home_teams, self.away_teams)

            if idx != -1:
                self.ordered_sim_games.append(self.sim_data[idx].copy())
                self.ordered_sim_labels.append(self.sim_labels[idx].copy())
            else:
                print("Error")
        



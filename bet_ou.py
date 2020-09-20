from neural_net import NN
import numpy as np

rede = "models_hda/PO11_money"
n_outputs = 2



#       GR  DE  DC  DC  DC  DD MDC MDC  ME  MC  MC  MC  MD MCO MCO  EE  PL  PL  ED
data = [75,  0, 77, 77, 75,  0,  0,  0, 75,  0,  0,  0, 60, 78,  0,  0, 76, 78,  0,
        
        83, 81, 80, 81,  0, 75,  0,  0,  0, 79, 89, 84,  0,  0,  0, 79, 86,  0, 84]
        
odds = [5.65, 4.33, 1.56]
bankroll = 51.93

bet_amount = 0.00
RESULT_NAMES = ["Over 2.5", "Under 2.5"]

def find_value(probs, odds):
        value = []
        print(probs)
        print(odds)
        if (probs[0]*odds[0]-1) > 0:
            value.append((probs[0]*odds[0]-1, 0))
        if (probs[1]*odds[1]-1) > 0:
            value.append((probs[1]*odds[1]-1, 1))
    
        return max(value) if value != [] else 0
        
def get_bet_amount(bankroll, fraction, prob, odds):
    overlay = (prob*odds-1)
    return (bankroll*fraction)*(overlay/(odds-1))

neural_net = NN(n_outputs)

neural_net.load_model(rede)

# prediction_probs = neural_net.predict_single(data)
prediction_probs = neural_net.model.predict(np.array([data]) / 100.0)[0]
print(prediction_probs)
prediction = np.argmax(prediction_probs)
value = find_value(prediction_probs, odds)

if (value != 0 and value[1] == prediction):
            bet_amount = get_bet_amount(bankroll, 0.1, prediction_probs[value[1]], odds[value[1]])
            
if bet_amount != 0 and odds[value[1]] >= 1.2:
    print("Prediction:", RESULT_NAMES[prediction])
    print("Prediction probs:", prediction_probs[value[1]])
    print("Bet Amount: ", bet_amount)

else:
    print("Not Betting on this game!") 
"""
 https://leetcode.com/problems/shopping-offers/description/
 """
 
 class Solution:
     def shoppingOffers(self, price, special, needs):
         """
         :type price: List[int]
         :type special: List[List[int]]
         :type needs: List[int]
         :rtype: int
         """
         number_of_items = len(price)
         states = {}
 
         for offer in special:
             offer_state = offer[0:number_of_items]
             offer_price = offer[-1]
 
             offer_state_key = self.convert_to_key(offer_state)
 
             if offer_state_key in states:
                 offer_price = min(offer_price, states[offer_state_key]["price"])
 
             states[offer_state_key] = {
                 "price": offer_price,
                 "state": offer_state
             }
 
         return self.compute_best_price(states, {}, needs, price)
 
     def convert_to_key(self, state):
         return "".join(str(i) for i in state)
 
     def compute_worst_price(self, needs, individual_prices):
         price = 0
         for i,v in enumerate(needs):
             price += needs[i] * individual_prices[i]
 
         return price
 
     def compute_best_price(self, original_offers, all_states, needs, individual_prices):
         if needs == [0] * len(needs):
             return 0
 
         needs_key = self.convert_to_key(needs)
 
         # If the state already exists - return
         if needs_key in all_states:
             return all_states[needs_key]["price"]
 
         # Compute
         best_price = self.compute_worst_price(needs, individual_prices)
         new_needs = []
         for offer_key in original_offers.keys():
             offer = original_offers[offer_key]
             valid_new_state = False
             new_needs = []
             for i, item_quantity in enumerate(offer["state"]):
                 quantity_left_for_item = needs[i] - item_quantity
 
                 if quantity_left_for_item < 0:
                     valid_new_state = False
                     break
                 else:
                     new_needs.append(quantity_left_for_item)
                     valid_new_state = True
 
             if valid_new_state:
                 new_price = offer["price"] + self.compute_best_price(original_offers, all_states, new_needs, individual_prices)
                 best_price = min(
                     best_price,
                     new_price
                 )
 
             # else just go to the next offer
 
         all_states[self.convert_to_key(new_needs)] = {
             "state": new_needs,
             "price": best_price
         }
 
         return best_price


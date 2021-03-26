### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # Needs == symbol to test for equality
    if card.value = 1:
      return True
    # Needs colon after the else
    else
      return False
   
  # typo dif should be def, also missing comma between card1 and card2
  dif highest_card(self, card1 card2):
  # indentation error, block below needs to be indented to the right
  if card1.value > card2.value:
  # variable below should be card1 instead of card
    return card
  else:
    return card2
  

# Indentation error. Needs to be indented to the right so held within CardGame class
def cards_total(self, cards):
  # total not defined properly needs to be set equal to something
  total
  for card in cards:
    total += card.value
    # indentation error. Return statement needs to be taken out of the for loop. Needs a space after the of
    # Also can't concatenate string and integer, total needs to be converted to string.
    return "You have a total of" + total
  
```

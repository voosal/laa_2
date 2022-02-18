# Lab 2 2
We were told to make navigation on the file with type json. There were 3 types of objects: dict, list, str. So I wrote a program to go through the all data.
```diff
1. When user runs he program, it asks him to enter name of the file:
```
```python
-------------------------------------
Enter the file name >>> twitter2.json    
```
``` diff
2. Then we receive something like this:
```
```python
-------------------------------------
The item is a dictionary that has  6  elements
-------------------------------------
Here are all the keys:
Key: users
Key: next_cursor
Key: next_cursor_str
Key: previous_cursor
Key: previous_cursor_str
Key: total_count
Please, select the key: >>>
```
```diff
3. After this we get a data (if it was entered right) and it repeats again and again by the time the file is ended.
```
```diff
4. Also I processed possibble mistakes:
```
## File is not find
```python
-------------------------------------
The file doesn't exist(
-------------------------------------
Enter the file name >>>
```
## Key/element is not in the file
```python
You didn't enter a key from a dictinary
Please, select the key: >>>
```
# Conclusion 
___I learnt a lot about such a type of file like json, it was really interesting to work with it. Also I found out what kind of mistakes or problems can be. Finally I gain new experience.___

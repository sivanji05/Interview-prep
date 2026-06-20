
#MAX SPICES
from itertools import combinations
from bisect import bisect_left

def solve(n, spices, target):
    def get_sums(arr):
        sub_sums = []
        for s in range(len(arr) + 1):
            for c in combinations(arr, s):
                sub_sums.append(sum(c))
        return sub_sums
   
    left = spices[:n // 2]
    right = spices[n // 2:]
    
    left_sums = get_sums(left)
    right_sums = get_sums(right)
    
    
    right_sums.sort()
    
    
    min_diff = float("inf")
    

    for sum_left in left_sums:
        target_c = target - sum_left  
        
        
        idx = bisect_left(right_sums, target_c)
        
        
        if idx < len(right_sums):  
            min_diff = min(min_diff, abs(target - (sum_left + right_sums[idx])))
        
        if idx > 0:  
            min_diff = min(min_diff, abs(target - (sum_left + right_sums[idx - 1])))
    
    return min_diff



# TESURE DIVISION


def solve(n, k, nums):
    treasure_map = {id: value for id, value in nums}
    
    sorted_ids = sorted(treasure_map.keys())
   
    max_value = 0
    best_start = best_end = None
    
    current_value = 0
    window_start = 0

    for window_end in range(len(sorted_ids)):
        current_id = sorted_ids[window_end]
        current_value += treasure_map[current_id]  # Add current value to the window sum
        
        
        while current_id - sorted_ids[window_start] + 1 > k:
            current_value -= treasure_map[sorted_ids[window_start]]
            window_start += 1
        
        
        window_length = window_end - window_start + 1
    
        total_value = current_value + (k - window_length)
        
       
        if total_value > max_value:
            max_value = total_value
            best_start = sorted_ids[window_start]
            best_end = sorted_ids[window_end]
        elif total_value == max_value:
            if sorted_ids[window_start] < best_start:
                best_start = sorted_ids[window_start]
                # best_start =min(best_start,sorted_ids[window_start])
                best_end = sorted_ids[window_end]
    return [max_value, (best_end - k) + 1]

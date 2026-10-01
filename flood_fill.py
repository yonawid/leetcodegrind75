#flood fill 
from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """
        Time Complexity: O(m * n)
        - In the worst case, we might have to paint every single pixel in the grid.
        
        Space Complexity: O(m * n)
        - If we paint every pixel, the recursive call stack could grow to be the 
          size of the entire grid before it finishes.
        """
        # 1. Figure out what color we are allowed to paint over
        original_color = image[sr][sc]
        
        # 2. Edge Case: If it's already the right color, don't do anything!
        # (This prevents an infinite loop of painting the same spot)
        if color == original_color:
            return image
            
        # 3. Our robotic paint function
        def paint(r, c):
            # BASE CASE: Stop if we go off the edge of the picture, 
            # OR if we hit a pixel that isn't the original color.
            # BASE CASE / "STOP SIGNS":
            # 1. r < 0: Robot stepped off the TOP edge of the grid
            # 2. r >= len(image): Robot stepped off the BOTTOM edge
            # 3. c < 0: Robot stepped off the LEFT edge
            # 4. c >= len(image[0]): Robot stepped off the RIGHT edge
            # 5. image[r][c] != original_color: Robot stepped on a wrong color (or an already painted pixel)
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return 

                
            # If we survived the checks, paint the pixel!
            image[r][c] = color   
    
            # Send clones out to paint in all 4 directions
            paint(r + 1, c) # Down
            paint(r - 1, c) # Up
            paint(r, c + 1) # Right
            paint(r, c - 1) # Left
            
        # 4. Press the start button to kick off the painting at the starting coordinates
        paint(sr, sc)
        
        # 5. Return our freshly painted masterpiece
        return image



    def floodFill2(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        # 1. Identify the color we are starting on
        original_color = image[sr][sc]
        
        # 2. Early Exit: If the starting pixel is already the target color, do nothing!
        if original_color == color:
            return image
        # 3. The To-Do List (Queue). We use deque because it's fast like a grocery store line.
        # We package the starting row (sr) and column (sc) into a tuple and put it in the line.
        store = deque([(sr, sc)])
        
        # 4. The First Drop of Paint: Change the color immediately so we don't accidentally
        # put this exact same pixel back into the queue later.
        image[sr][sc] = color
        
        # 5. The Engine: Keep processing as long as there is a coordinate waiting in the To-Do list.
        while store:
            
            # Take the next set of coordinates off the FRONT of the line
            r, c = store.popleft()
            
            # 6. Look at the 4 neighbors touching this pixel (Down, Up, Right, Left)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = r + dr
                new_c = c + dc
                
                # 7. The Bouncers: Check the ID of the neighbor before adding them to the list.
                # - Are they off the edge of the grid? (< 0 or >= len)
                # - Are they a wall/different color? (!= original_color)
                if new_r < 0 or new_r >= len(image) or new_c < 0 or new_c >= len(image[0]) or image[new_r][new_c] != original_color:
                    continue # Kick them out (skip this neighbor and move to the next one)
                # 8. If they passed the bouncers, paint them immediately!
                image[new_r][new_c] = color
                
                # 9. Add them to the back of the To-Do list so THEIR neighbors can be checked later.
                store.append((new_r, new_c))
            
        # 10. The To-Do list is empty, the paint has spread everywhere it can. We are done!
        return image

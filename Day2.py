# This solution is flawed
class Solution:
    List = []
    def parse_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                # Strip the newline character at the end of the line
                line = line.strip()
                # Extract characters at the specified indices
                list = line.split(" ")
                self.List.append(list)
        return
    def isSorted(self, arr) -> bool:
        if sorted(arr) == arr or sorted(arr, reverse=True) == arr:
            return True
        else:
            return False
    def RemoveFailed(self):
        updatedList = self.List
        j = 0
        for num in range(len(self.List)):
            if self.isSorted(self.List):
                for i in range(1, len(self.List))
                        pass
                 else:
                        updatedList.pop(j)
                        break
            else:
                updatedList.pop(j)
            j+=1
        self.List = updatedList
    def numOfSafe(self):
        count = 0
        for list in self.List:
            count+=1
        return count
        
# Example usage
solution = Solution()
file_path = 'input2.txt'  # Replace with your file path
solution.parse_file(file_path)
solution.RemoveFailed()
print(solution.numOfSafe())
print("Completed")

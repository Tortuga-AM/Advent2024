class Solution:
    List1 = []
    List2 = []
    def parse_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                # Strip the newline character at the end of the line
                line = line.strip()
                # Extract characters at the specified indices
                self.List1.append(line[0:5])
                self.List2.append(line[8:13])
        return
    def SortLists(self):
        self.List1.sort()
        self.List2.sort()
        return
    def doSubtraction(self):
        i=0
        result = []
        for item in self.List1:
            result.append(abs(int(item)-int(self.List2[i])))
            i+=1
        return result
    def printAddedResult(self, result):
        count = 0
        for item in result:
            count += item
        print(count)
        return
    def compareLists(self):
        similarity_score = 0
        for number in self.List1:
            count = 0
            for number2 in self.List2:
                if int(number) == int(number2):
                    count+=1
            similarity_score+=count*int(number)
        return similarity_score

        
# Example usage
solution = Solution()
file_path = 'input1.txt'  # Replace with your file path
solution.parse_file(file_path)
solution.SortLists()
result = solution.doSubtraction()
solution.printAddedResult(result)
score = solution.compareLists()
print(score)

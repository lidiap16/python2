def ave(grade1, grade2):
    average = (grade1 + grade2) / 2
    print("average= ", average)
    
test_cases = [
    {"input1": 3, "input2": 5, "expected": "your average is 4"}
    
]
def test_ave():
    for case in test_cases:
            try:
                print("Testing with input:", {case['input1']}, {case['input2']} )
                ave(case['input1'], case['input2'])
                print("Expected output:", {case['expected']})
            except Exception as e:
                print("Error:", {e})
                print("Expected output:", {case['expected']})

test_ave()
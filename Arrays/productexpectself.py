def productExceptSelf(nums):
    preArray = [ 1 for z in range(len(nums))]
    sufArray = [ 1 for z in range(len(nums))]

    lengthIdx = len(nums) -1 
    for idx in range(lengthIdx,-1,-1):
        if idx == lengthIdx:
            sufArray[idx] = 1
        else: 
            sufArray[idx] = nums[idx+1] * sufArray[idx+1]
            print(sufArray[idx])

    print(sufArray)

    for idx in range(len(nums)):
        if idx == 0:
            preArray[idx] = 1
        else: 
            preArray[idx] = nums[idx-1] * preArray[idx-1]

    print(preArray)

    productArray = []

    for idx in range(len(nums)):
        productArray.append(preArray[idx]*sufArray[idx])

    return productArray

print(productExceptSelf([-1,1,0,-3,3]))
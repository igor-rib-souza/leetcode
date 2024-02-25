class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        j = 0
        k = 0
        array = []        

        for i in range(len(nums1)+len(nums2)):
            if(j >= len(nums1)):
                array.append(nums2[k])
                k+=1
            elif(k >= len(nums2)):
                array.append(nums1[j])
                j+=1
            elif (nums1[j]>nums2[k]):
                array.append(nums2[k])
                k+=1
            else:
                array.append(nums1[j])
                j+=1
        if ((j+k)%2==0):
            return (array[(j+k)//2] + array[((j+k)//2)-1])/2
        else:
            return array[(j+k)//2]
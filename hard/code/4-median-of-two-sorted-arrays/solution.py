class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        j = 0
        k = 0
        ar = []        

        for i in range(len(nums1)+len(nums2)):
            if(j >= len(nums1)):
                ar.append(nums2[k])
                k+=1
            elif(k >= len(nums2)):
                ar.append(nums1[j])
                j+=1
            elif (nums1[j]>nums2[k]):
                ar.append(nums2[k])
                k+=1
            else:
                ar.append(nums1[j])
                j+=1
                
        s = j+k
        if ((j+k)%2==0):
            return (ar[s//2] + ar[(s//2)-1])/2
        else:
            return ar[s//2]
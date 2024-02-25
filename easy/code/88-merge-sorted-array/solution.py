class Solution:
    def merge(self, nums1: List[int], m: int, nums2:List[int], n: int) -> None:       
       
        j = m-1
        k = n-1
        
        t = m+n-1
        
        while j >= 0 and k >= 0:
            if nums1[j] > nums2[k]:
                nums1[t] = nums1[j]
                j -= 1
            else:
                nums1[t] = nums2[k]
                k -= 1
            t -= 1
            
        nums1[:k + 1] = nums2[:k + 1]
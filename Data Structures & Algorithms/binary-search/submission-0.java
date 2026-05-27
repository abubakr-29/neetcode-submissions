class Solution {
    public int search(int[] nums, int target) {
        int lb = 0; 
        int ub = nums.length - 1;

        while (lb <= ub) { 
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] < target) {
                lb = mid + 1; 
            } else if (nums[mid] > target) {
                ub = mid - 1;
            } else {
                return mid; 
            }
    }

    return -1;
    }
}

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        if(root==null||(root.left==null&&root.right==null))
            return true;
        q.add(root);
        while(!q.isEmpty()){
            int s=q.size();
            ArrayList<Integer> valArr = new ArrayList<>();
            for(int i=0;i<s;i++){
                if(q.peek().left!=null){
                    q.add(q.peek().left);
                    valArr.add(q.peek().left.val);
                }
                else{
                    valArr.add(-1);
                }
                if(q.peek().right!=null){
                    q.add(q.peek().right);
                    valArr.add(q.peek().right.val);
                }
                else{
                    valArr.add(-1);
                }
                q.remove();
            }
            for(int i=0;i<valArr.size();i++)
            {
                if(valArr.get(i)!=valArr.get(valArr.size()-1-i))
                    return false;
            }
        }
        return true;
            
    }
}
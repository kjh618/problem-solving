// Python 3 was too slow

use std::io;

const MATCHES: [(usize, usize); 15] = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5),
];

fn generate_results_and_check(
    m: usize,
    result: &mut [u32; 18],
    inputs: &[Vec<u32>; 4],
    ans: &mut [u8; 4],
) {
    if m == MATCHES.len() {
        for i in 0..4 {
            if result == inputs[i].as_slice() {
                ans[i] = 1;
            }
        }
        return;
    }

    let (t1, t2) = MATCHES[m];
    let (t1, t2) = (t1 * 3, t2 * 3);

    // t1 win, t2 lose
    result[t1 + 0] += 1;
    result[t2 + 2] += 1;
    generate_results_and_check(m + 1, result, inputs, ans);
    result[t1 + 0] -= 1;
    result[t2 + 2] -= 1;

    // draw
    result[t1 + 1] += 1;
    result[t2 + 1] += 1;
    generate_results_and_check(m + 1, result, inputs, ans);
    result[t1 + 1] -= 1;
    result[t2 + 1] -= 1;

    // t1 lose, t2 win
    result[t1 + 2] += 1;
    result[t2 + 0] += 1;
    generate_results_and_check(m + 1, result, inputs, ans);
    result[t1 + 2] -= 1;
    result[t2 + 0] -= 1;
}

fn main() {
    const EMPTY_VEC: Vec<u32> = Vec::new();
    let mut inputs = [EMPTY_VEC; 4];
    for i in 0..4 {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        let input: Vec<u32> = input
            .split_ascii_whitespace()
            .map(|n| n.parse().unwrap())
            .collect();

        inputs[i] = input;
    }

    let mut ans = [0; 4];
    let mut result = [0; 18];
    generate_results_and_check(0, &mut result, &inputs, &mut ans);

    for a in &ans {
        print!("{} ", a);
    }
    println!();
}

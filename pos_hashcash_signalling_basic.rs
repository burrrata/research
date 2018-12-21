/*
 PoS HashCash Style Pricing and Review System
 - the producer has a stake because they're 
   vouching that the thing they're creating is worth 
   what they're charging and if not they'll issue a refund
 - the consumer is staking their capital (and time) to try
   an experience or product, but they can receive a
   portion of their initial stake back if they are dissatisfied
 
 This example is in the style of an artist publicly stating that
 their show/album/movie/thing is X number of stars in awesomeness.
 This way, if they're just trying something out, the audience can
 come with that expectation, and if it's a full mainstream release
 then that can be factored in as well.
 
 If people feel like the show/thing was worse than
 advertised: give them a refund proportional the amount
 they thought it was worse.
 
 If people feel like the show/thing was better than
 advertised: suggest a donation proportional to the amount 
 they thought it was better.
*/

fn main() {
    // Artist Defined Metrics
    // public star rating
    let psr: f64 = 7.0;
    // public price
    let pp: f64 = 10.0;
    
    // Your Metrics
    // your star rating
    let ysr: f64 = 8.0;
    // function to calculate your price difference
    fn personal_pricing(psr: f64,
                        pp: f64,
                        ysr: f64) -> f64 {
        // multiply the star rating by 0.1 to make the delta a %
        // where each star is weighted at 10%  
        let my_delta = 0.1_f64 * (psr - ysr); 
        let yp_dif = my_delta * pp;
        yp_dif
    }
    // your price difference from the public price
    let ypd = personal_pricing(psr, pp, ysr);
    
    // Print Results
    if ypd < 0.0 {
        println!("We're so glad you enjoyed the show! If you thought that it was worth more than you paid, please consider making a donation of {:?}. Thanks!", -ypd);
    } else if ypd > 0.0 {
        println!("We're sorry you did not enjoy the show. Please accept this refund of {:?} to show our sincere apologies.", ypd);
    } else {
        println!("We hope you enjoyed the show! :)")
    }
}

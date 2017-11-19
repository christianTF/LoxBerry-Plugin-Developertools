#!/usr/bin/perl

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


##########################################################################
# Modules
##########################################################################
use FindBin;
use lib "$FindBin::Bin/./perllib";
use LoxBerry::System;
use LoxBerry::Web;

# Version of this script
our $version = LoxBerry::System::pluginversion();

use CGI::Carp qw(fatalsToBrowser);
use CGI qw/:standard/;
use Config::Simple;
use HTML::Template;
use warnings;
use strict;
no strict "refs"; # we need it for template system and for contructs like ${"skalar".$i} in loops

##########################################################################
# Variables
##########################################################################
our  $cgi = CGI->new;
my  $pcfg;
my  $lang;
my  $languagefile;
my  $pname;
my  $languagefileplugin;
my  %TPhrases;
my $topmenutemplate;
my $maintemplate;
my $footertemplate;

my $dd_backup_command;
my $tgz_backup_command;
my $rsync_backup_command;

our @backuptypes = ('DD', 'RSYNC', 'TGZ');

##########################################################################
# Read Settings
##########################################################################

 my $datestring = localtime();
 print STDERR "========== LoxBerry Backup Version $version === ($datestring) =========\n";
 print STDERR "Global variables from LoxBerry::System\n";
 print STDERR "Homedir:     $lbhomedir\n";
 print STDERR "Plugindir:   $lbplugindir\n";
 print STDERR "CGIdir:      $lbcgidir\n";
 print STDERR "HTMLdir:     $lbhtmldir\n";
 print STDERR "Templatedir: $lbtemplatedir\n";
 print STDERR "Datadir:     $lbdatadir\n";
 print STDERR "Logdir:      $lblogdir\n";
 print STDERR "Configdir:   $lbconfigdir\n";

# Start with HTML header
print $cgi->header(
         -type    =>      'text/html',
         -charset =>      'utf-8'
);

# Get language from GET, POST or System setting (from LoxBerry::Web)
$lang = lblanguage();

##########################################################################
# Initialize html templates
##########################################################################

# See http://www.perlmonks.org/?node_id=65642
		
##########################################################################
# Print Template
##########################################################################

# In LoxBerry V0.2.x we use the old LoxBerry::Web header
LoxBerry::Web::lbheader("Developer Plugin V$version", "http://www.loxwiki.eu:80/x/vICO");

print "<p>This plugin has nothing to configure in the Web UI.</p>";
print "<p>If you have some cool tweaks that I could integrate, let me know!</p>";

LoxBerry::Web::lbfooter();

exit;

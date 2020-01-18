Summary: Get number of occupied columns of a string on terminal
Name: perl-Text-CharWidth
Version: 0.04
Release: 18%{?dist}
License: GPL+ or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Text-CharWidth/
Source0: http://search.cpan.org/CPAN/authors/id/K/KU/KUBOTA/Text-CharWidth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(XSLoader)
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This is a module to provide equivalent feature as wcwidth(3) and
wcswidth(3).  This also provides mblen(3) equivalent subroutine.

%prep
%setup -q -n Text-CharWidth-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -type f \( -name .packlist -or -name perllocal.pod \
  -or \( -name '*.bs' -a -empty \) \) -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} \;
chmod -R u+w %{buildroot}

%check
make test

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README Changes
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/man3/Text::CharWidth.3pm*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.04-18
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.04-17
- Mass rebuild 2013-12-27

* Fri Oct 26 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-16
- Specify all dependencies.
- Add default filter.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.04-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.04-12
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-10
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-9
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.04-8
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 24 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.04-5
- %%check || : does not work anymore.

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-2.2
- add BR: perl(Test::Simple)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Dec 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.04-2
- Add ownership of some perl folders.

* Thu Dec 28 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.04-1
- Initial build.

